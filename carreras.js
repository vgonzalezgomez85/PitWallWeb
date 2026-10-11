/* PitWall Web — Buscador de carreras de slot.
   Lee dos ficheros y los mezcla en el navegador:
     datos/carreras-manuales.json  → las que añades tú a mano (van en el repo)
     datos/carreras-auto.json      → las que encuentra la IA (las genera el servidor)
   Si una carrera manual tiene el mismo id que una de la IA, gana la manual.
   AGPLv3 o posterior. Véase LICENSE. */
(function(){
  var LANG = (document.documentElement.lang || 'es').slice(0,2);
  var D = {
    es:{tipos:{resistencia:'Resistencia',velocidad:'Velocidad',rally:'Rally',raid:'Raid',otro:'Otros'},
        all:'Todos',allC:'Todos los campeonatos',results:function(n){return n===1?'1 carrera':n+' carreras';},
        updated:'Búsqueda automática actualizada',never:'sin búsqueda automática todavía',
        ok:'Verificada',ai:'Encontrada por IA',web:'Web',none:'No hay carreras con estos filtros.',
        err:'No se ha podido cargar el calendario.',races:function(n){return n===1?'1 carrera':n+' carreras';}},
    en:{tipos:{resistencia:'Endurance',velocidad:'Sprint',rally:'Rally',raid:'Raid',otro:'Other'},
        all:'All',allC:'All championships',results:function(n){return n===1?'1 race':n+' races';},
        updated:'Automatic search updated',never:'no automatic search yet',
        ok:'Verified',ai:'Found by AI',web:'Website',none:'No races match these filters.',
        err:'The calendar could not be loaded.',races:function(n){return n===1?'1 race':n+' races';}},
    fr:{tipos:{resistencia:'Endurance',velocidad:'Vitesse',rally:'Rallye',raid:'Raid',otro:'Autres'},
        all:'Tous',allC:'Tous les championnats',results:function(n){return n===1?'1 course':n+' courses';},
        updated:'Recherche automatique mise à jour',never:'pas encore de recherche automatique',
        ok:'Vérifiée',ai:'Trouvée par l’IA',web:'Site',none:'Aucune course ne correspond à ces filtres.',
        err:'Impossible de charger le calendrier.',races:function(n){return n===1?'1 course':n+' courses';}},
    it:{tipos:{resistencia:'Endurance',velocidad:'Velocità',rally:'Rally',raid:'Raid',otro:'Altro'},
        all:'Tutti',allC:'Tutti i campionati',results:function(n){return n===1?'1 gara':n+' gare';},
        updated:'Ricerca automatica aggiornata',never:'nessuna ricerca automatica ancora',
        ok:'Verificata',ai:'Trovata dall’IA',web:'Sito',none:'Nessuna gara con questi filtri.',
        err:'Impossibile caricare il calendario.',races:function(n){return n===1?'1 gara':n+' gare';}}
  };
  var T = D[LANG] || D.es;

  var $ = function(id){return document.getElementById(id);};
  var qEl=$('f-q'), paisEl=$('f-pais'), tipoEl=$('f-tipo'), campEl=$('f-camp'), pastEl=$('f-past'),
      listEl=$('list'), countEl=$('count'), updEl=$('updated');

  var fmtMonth = new Intl.DateTimeFormat(LANG,{month:'long',year:'numeric'});
  var fmtWd = new Intl.DateTimeFormat(LANG,{weekday:'short'});
  var regionNames = null;
  try{ regionNames = new Intl.DisplayNames([LANG],{type:'region'}); }catch(e){}
  function country(code){
    if(!code) return '';
    try{ return regionNames ? regionNames.of(code.toUpperCase()) : code; }catch(e){ return code; }
  }
  function flag(code){
    if(!/^[A-Za-z]{2}$/.test(code||'')) return '';
    return String.fromCodePoint.apply(null, code.toUpperCase().split('').map(function(c){return 127397+c.charCodeAt(0);}));
  }
  function parseDate(s){ // "AAAA-MM-DD" en hora local, sin desfases de zona horaria
    var m=/^(\d{4})-(\d{2})-(\d{2})$/.exec(s||''); return m ? new Date(+m[1],m[2]-1,+m[3]) : null;
  }
  function norm(s){ return (s||'').toString().toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,''); }
  function slug(s){ return norm(s).replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,''); }
  function esc(s){ return (s||'').toString().replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];}); }
  function safeUrl(u){ return /^https?:\/\//i.test(u||'') ? u : ''; }
  function idOf(r){ return r.id || [slug(r.campeonato||r.nombre), r.fecha, slug(r.ciudad||r.club)].filter(Boolean).join('-'); }
  function dayKey(r){ return slug(r.campeonato||r.nombre)+'|'+r.fecha; }

  function load(url){
    return fetch(url,{cache:'no-cache'}).then(function(r){ return r.ok ? r.json() : null; }).catch(function(){ return null; });
  }

  var ALL = [];
  Promise.all([load('datos/carreras-manuales.json'), load('datos/carreras-auto.json')]).then(function(res){
    var man = res[0] || {}, auto = res[1] || {};
    if(!res[0] && !res[1]){ listEl.innerHTML='<div class="empty">'+esc(T.err)+'</div>'; return; }
    var hidden = {}; (man.ocultar||[]).forEach(function(id){ hidden[id]=1; });
    // Si ya hay carreras verificadas de un campeonato en una fecha, las de la IA para ese mismo día sobran.
    var manDays = {}; (man.carreras||[]).forEach(function(r){ manDays[dayKey(r)]=1; });
    var byId = {};
    (auto.carreras||[]).forEach(function(r){ r._src='ai'; r.id=idOf(r); if(!hidden[r.id] && !manDays[dayKey(r)]) byId[r.id]=r; });
    (man.carreras||[]).forEach(function(r){ r._src='ok'; r.id=idOf(r); byId[r.id]=r; });
    ALL = Object.keys(byId).map(function(k){ return byId[k]; })
      .filter(function(r){ return parseDate(r.fecha); })
      .sort(function(a,b){ return a.fecha<b.fecha?-1:a.fecha>b.fecha?1:(a.nombre||'').localeCompare(b.nombre||''); });

    if(auto.generado){
      var d = new Date(auto.generado);
      updEl.textContent = T.updated+': '+d.toLocaleDateString(LANG,{day:'numeric',month:'short',year:'numeric'});
    } else updEl.textContent = T.never;

    fillSelects(); readHash(); render();
  });

  function fillSelects(){
    var paises={}, camps={};
    ALL.forEach(function(r){ if(r.pais) paises[r.pais.toUpperCase()]=1; if(r.campeonato) camps[r.campeonato]=1; });
    var tipos={}; ALL.forEach(function(r){ if(r.tipo) tipos[r.tipo]=1; });
    tipoEl.innerHTML = '<option value="">'+esc(T.all)+'</option>' + ['resistencia','velocidad','rally','raid','otro']
      .filter(function(k){return tipos[k];})
      .map(function(k){return '<option value="'+k+'">'+esc(T.tipos[k])+'</option>';}).join('');
    paisEl.innerHTML = '<option value="">'+esc(T.all)+'</option>' + Object.keys(paises)
      .sort(function(a,b){return country(a).localeCompare(country(b),LANG);})
      .map(function(p){return '<option value="'+p+'">'+flag(p)+' '+esc(country(p))+'</option>';}).join('');
    campEl.innerHTML = '<option value="">'+esc(T.allC)+'</option>' + Object.keys(camps)
      .sort(function(a,b){return a.localeCompare(b,LANG);})
      .map(function(c){return '<option value="'+esc(c)+'">'+esc(c)+'</option>';}).join('');
  }

  // Los filtros se guardan en la URL (#pais=ES&camp=Resisbarna) para poder compartir el enlace.
  function readHash(){
    var p = new URLSearchParams(location.hash.slice(1));
    if(p.get('q')) qEl.value=p.get('q');
    if(p.get('pais')) paisEl.value=p.get('pais');
    if(p.get('tipo')) tipoEl.value=p.get('tipo');
    if(p.get('camp')) campEl.value=p.get('camp');
    pastEl.checked = p.get('pasadas')==='1';
  }
  function writeHash(){
    var p = new URLSearchParams();
    if(qEl.value.trim()) p.set('q',qEl.value.trim());
    if(paisEl.value) p.set('pais',paisEl.value);
    if(tipoEl.value) p.set('tipo',tipoEl.value);
    if(campEl.value) p.set('camp',campEl.value);
    if(pastEl.checked) p.set('pasadas','1');
    var h = p.toString();
    history.replaceState(null,'',h ? '#'+h : location.pathname+location.search);
  }

  function render(){
    var today = new Date(); today.setHours(0,0,0,0);
    var q = norm(qEl.value.trim()), pais=paisEl.value, tipo=tipoEl.value, camp=campEl.value, past=pastEl.checked;
    var rows = ALL.filter(function(r){
      var end = parseDate(r.fecha_fin) || parseDate(r.fecha);
      if(!past && end < today) return false;
      if(pais && (r.pais||'').toUpperCase()!==pais) return false;
      if(tipo && r.tipo!==tipo) return false;
      if(camp && r.campeonato!==camp) return false;
      if(q && norm([T.tipos[r.tipo],r.nombre,r.campeonato,r.club,r.ciudad,r.circuito,r.categoria,country(r.pais)].join(' ')).indexOf(q)<0) return false;
      return true;
    });
    countEl.innerHTML = '<b>'+esc(T.results(rows.length))+'</b>';
    if(!rows.length){ listEl.innerHTML='<div class="empty">'+esc(T.none)+'</div>'; return; }

    var groups = [], cur = null;
    rows.forEach(function(r){
      var k = r.fecha.slice(0,7);
      if(!cur || cur.k!==k){ cur={k:k,items:[]}; groups.push(cur); }
      cur.items.push(r);
    });
    listEl.innerHTML = groups.map(function(g){
      var m = fmtMonth.format(parseDate(g.k+'-01'));
      return '<h2 class="month">'+esc(m)+' <small>'+esc(T.races(g.items.length))+'</small></h2>' + g.items.map(function(r){
        var d1=parseDate(r.fecha), d2=parseDate(r.fecha_fin), end=d2||d1;
        var day = d1.getDate() + (d2 && +d2!==+d1 ? '<i>–'+d2.getDate()+'</i>' : '');
        var place = [r.circuito||r.club, r.ciudad, r.pais ? flag(r.pais)+' '+country(r.pais) : ''].filter(Boolean).map(esc).join(' · ');
        var url = safeUrl(r.enlace);
        return '<article class="race'+(end<today?' past':'')+'">'+
          '<div class="date"><div class="d">'+day+'</div><div class="w">'+esc(fmtWd.format(d1))+'</div></div>'+
          '<div class="info"><h3>'+esc(r.nombre||r.campeonato)+'</h3>'+
            '<div class="tags">'+
              (r.campeonato && r.campeonato!==r.nombre ? '<span class="tag champ">'+esc(r.campeonato)+'</span>' : '')+
              (T.tipos[r.tipo] ? '<span class="tag">'+esc(T.tipos[r.tipo])+'</span>' : '')+
              (r.categoria ? '<span class="tag">'+esc(r.categoria)+'</span>' : '')+
              (r.escala ? '<span class="tag">'+esc(r.escala)+'</span>' : '')+
              '<span class="tag '+r._src+'">'+esc(r._src==='ok'?T.ok:T.ai)+'</span>'+
            '</div>'+
            (place ? '<div class="place">'+place+'</div>' : '')+
            (r.notas ? '<div class="notes">'+esc(r.notas)+'</div>' : '')+
          '</div>'+
          (url ? '<a class="go" href="'+esc(url)+'" target="_blank" rel="noopener nofollow">'+esc(T.web)+' ↗</a>' : '<span></span>')+
        '</article>';
      }).join('');
    }).join('');
  }

  [qEl,paisEl,tipoEl,campEl,pastEl].forEach(function(el){
    el.addEventListener(el===qEl?'input':'change',function(){ writeHash(); render(); });
  });
})();
