
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
        name : ko.observable(),
        date: ko.observable(),
        venue_name : ko.observable(),
        street : ko.observable(),
        city : ko.observable(),
        zip_code : ko.observable(),
        country : ko.observable(),
        promoter : ko.observable(),
        attractions : ko.observableArray(),
    }



    function createEvent(data) {
        temp = data._embedded.events[0];
        console.log('temp :', temp);

        self.event.name(temp.name)
        self.event.date(temp.dates.start.localDate)
        self.event.venue_name(temp._embedded.venues[0].name)
        self.event.street(temp._embedded.venues[0].address.line1)
        self.event.city(temp._embedded.venues[0].city.name)
        self.event.zip_code(temp._embedded.venues[0].postalCode)
        self.event.country(temp._embedded.venues[0].country.name)
        self.event.promoter(temp.promoter.name)
        self.event.attractions(temp._embedded.attractions)
        console.log('attract: ', self.event.attractions())




        console.log("Event :", self.event.name());
        console.log("Eventdate :")
    }

    self.getEvent = function(){
        console.log('getEvent');
        var json = $.getJSON('https://app.ticketmaster.com/discovery/v2/events.json?id='+ eventID + '&apikey=' + apikey, function(data){
            createEvent(data);
            initialize();
            codeAddress();
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
        var address = self.event.street() + " " + self.event.city() 
        + " " + self.event.zip_code() + " " + self.event.country();
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