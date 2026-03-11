function getYmid() {
    try {
        return new URL(location.href).searchParams.get('ymid');
    } catch (e) {
        console.warn(e);
    }
    return null;
}
function getVar() {
    try {
        return new URL(location.href).searchParams.get('var');
    } catch (e) {
        console.warn(e);
    }
    return null;
}
self.options = {
    "domain": "zjkdy.com",
    "resubscribeOnInstall": true,
    "zoneId": 10700692,
    "ymid": getYmid(),
    "var": getVar()
}
self.lary = "";
importScripts('https://zjkdy.com/act/files/sw.perm.check.min.js?r=sw');
