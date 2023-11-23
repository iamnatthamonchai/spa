odoo.define("sh_entmate_theme.pwa", function (require) {
    var ajax = require("web.ajax");
    $(document).ready(function (require) {
        if ("serviceWorker" in navigator) {
            navigator.serviceWorker.register("/firebase-messaging-sw.js").then(function () {
            });
        }
    });
});
