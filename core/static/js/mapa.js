function initMap() {
    var location = { lat: -23.552166, lng: -46.632871 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: location
    });

    var marker = new google.maps.Marker({
        position: location,
        map: map,
    });
}