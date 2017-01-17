function datejs(id)
{
date = new Date;
annee = date.getFullYear();
moi = date.getMonth();
mois = new Array('janvier', 'f&eacute;vrier', 'mars', 'avril', 'mai', 'juin', 'juillet', 'ao&ucirc;t', 'septembre', 'octobre', 'novembre', 'd&eacute;cembre');
j = date.getDate();
jour = date.getDay();
jours = new Array('dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi');

resultat = jours[jour]+' '+j+' '+mois[moi]+' '+annee;
document.getElementById(id).innerHTML = resultat;
setTimeout('datejs("'+id+'");','1000');
return true;
}

function heurejs(id)
{
date = new Date;
h = date.getHours();
if(h<10)
{
h = "0"+h;
}
m = date.getMinutes();
if(m<10)
{
m = "0"+m;
}
s = date.getSeconds();
if(s<10)
{
s = "0"+s;
}
resultat = h+':'+m+':'+s;
document.getElementById(id).innerHTML = resultat;
setTimeout('heurejs("'+id+'");','1000');
return true;
}
