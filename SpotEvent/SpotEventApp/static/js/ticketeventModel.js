
var viewModel = new function()
{
    var self = this;
    var apikey = 'A491Blf11EgsYMWGiUGcgNA2rM3bDNtD';



    self.searchstring = ko.observable('');

    self.search = function(){
        window.location.href = "search/" + self.searchstring(); 
    }

    var url = window.location.href;
    var eventID = url.slice(34);
    console.log('ID :', eventID);

    self.event = {
        name : ko.observable()
    }



    function createEvent(data) {
        self.event.name(data._embedded.events[0].name);
        console.log("Event :");
        console.log("Eventdate :")
    }

    self.getEvent = function(){
        console.log('getEvent');
        var json = $.getJSON('https://app.ticketmaster.com/discovery/v2/events.json?id=Z698xZG2ZakoK&apikey=' + apikey, function(data){
            createEvent(data);
        })
    }

    self.getEvent();

    var geocoder;
    var map;
    function initialize() {
        geocoder = new google.maps.Geocoder();
        //var latlng = new google.maps.LatLng(-34.397, 150.644);
        var mapOptions = {
            zoom: 10,
            //center: latlng
        }
        map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);
    }
    function codeAddress() {
        var address = self.address.street() + " " + self.address.number() + " " + self.address.city() 
        + " " + self.address.zip_code() + " " + self.address.country();
        console.log("GOOGLE",address)
        geocoder.geocode( { 'address': address}, function(results, status) {
            if (status == 'OK') {
                map.setCenter(results[0].geometry.location);
                var marker = new google.maps.Marker({
                    map: map,
                    position: results[0].geometry.location
                });
            } else {
                alert('Geocode was not successful for the following reason: ' + status);
            }
        });
    }
}

ko.applyBindings(viewModel);  