// Monta una píldora: un clip por tramo (recorte + velocidad + rótulo) y luego los une.
// Uso: node render.js <píldora.json>
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const specFile = path.resolve(process.argv[2]);
const spec = JSON.parse(fs.readFileSync(specFile, 'utf8'));
const work = path.join(path.dirname(specFile), path.basename(specFile, '.json'));
const ov = path.join(work, 'ov');
fs.mkdirSync(ov, { recursive: true });
execFileSync('node', [path.join(__dirname, 'overlays.js'), specFile, ov], { stdio: 'inherit' });

const FPS = 30;
const ENC = ['-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(FPS),
  '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2'];
const ff = args => execFileSync('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', ...args], { stdio: 'inherit' });

const clips = [];
spec.segments.forEach((s, i) => {
  const out = path.join(work, `clip-${String(i).padStart(2, '0')}.mp4`);
  if (s.card) {
    const d = s.dur;
    ff(['-loop', '1', '-t', String(d), '-i', path.join(ov, `card-${i}.png`),
      '-f', 'lavfi', '-t', String(d), '-i', 'anullsrc=r=48000:cl=stereo',
      '-vf', `scale=1920:1080,format=yuv420p,fade=in:st=0:d=0.4,fade=out:st=${d - 0.4}:d=0.4`,
      '-shortest', ...ENC, out]);
  } else {
    const [x, y, w, h, mode] = spec.crops[s.crop];
    const dur = (s.to - s.from) / s.speed;
    // "fit": encaja la zona entera sin recortar, con franjas negras si no es 16:9
    const fit = mode === 'fit'
      ? 'scale=1920:1080:force_original_aspect_ratio=decrease:flags=lanczos,pad=1920:1080:(ow-iw)/2:(oh-ih)/2'
      : 'scale=1920:1080:flags=lanczos';
    let vf = `[0:v]crop=${w}:${h}:${x}:${y},${fit},setpts=(PTS-STARTPTS)/${s.speed},fps=${FPS}[v]`;
    const inputs = ['-ss', String(s.from), '-to', String(s.to), '-i', s.src || spec.source];
    if (s.caption) {
      inputs.push('-loop', '1', '-t', String(dur), '-i', path.join(ov, `cap-${i}.png`));
      vf += `;[1:v]format=rgba,fade=in:st=0.15:d=0.3:alpha=1[c];[v][c]overlay=0:0:shortest=1[o]`;
    }
    // Sonido del propio PitWall (semáforo, canto de tiempos) solo si el tramo lo pide
    if (s.audio) vf += `;[0:a]atempo=${s.speed},apad,aresample=48000[a]`;
    const audio = ['-map', s.audio ? '[a]' : `${s.caption ? 2 : 1}:a`];
    ff([...inputs, '-f', 'lavfi', '-t', String(dur), '-i', 'anullsrc=r=48000:cl=stereo',
      '-filter_complex', vf, '-map', s.caption ? '[o]' : '[v]', ...audio,
      '-t', String(dur), ...ENC, out]);
  }
  clips.push(out);
  console.log('tramo', i, 'listo');
});

const list = path.join(work, 'list.txt');
fs.writeFileSync(list, clips.map(c => `file '${c.replace(/'/g, "'\\''")}'`).join('\n'));
fs.mkdirSync(path.dirname(spec.output), { recursive: true });
ff(['-f', 'concat', '-safe', '0', '-i', list, '-c', 'copy', '-movflags', '+faststart', spec.output]);
console.log('→', spec.output);
