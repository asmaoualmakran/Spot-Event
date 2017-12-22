var viewModel = new function()
{
   var apikey = 'A491Blf11EgsYMWGiUGcgNA2rM3bDNtD';
    var self = this;

    var cookie = document.cookie;
    console.log('cookie :', cookie.slice(3))
    var userID = parseInt(cookie.slice(3));

    self.searchstring = ko.observable('');

    var url = window.location.href;

    self.search = function(){
        window.location.href = "search" + self.searchstring(); 
    }

    self.openEvent = function(id){
        window.location = "http://127.0.0.1:8000/event" + id;
    }

    self.openTicketEvent = function(id){
        window.location = "http://127.0.0.1:8000/ticketevent" + id;
    }

    self.sortf = function(a, b){
    	var aDate = a.event_date;
    	var bDate = b.event_date;
    	return ((aDate < bDate) ? -1 : ((aDate > bDate) ? 1 : 0));
    }

    self.events = ko.observableArray();
    self.ticketmaster = ko.observableArray();

    function createEvents(data) {
        self.events(data);
    }

    function createTicketmaster(data) {
    	if(data.page.totalElements > 0){
    		self.ticketmaster(data._embedded.events);
    	}
    }

    self.getEvents = function(){
        var json = $.getJSON('/api/event',function(data){
            console.log('Events:',data);
            data.map(el => el.venue = {'address': {'street' : ''}});
            data2 = data.sort(self.sortf);
            console.log('Sorted :', data2);
            self.getVenues(data2);
            console.log('venues added :', self.events());
            //self.getUsers();
            console.log('user added :', self.events());
        });
    }

    self.getTicketmaster = function(){
    	var json = $.getJSON('https://app.ticketmaster.com/discovery/v2/events.json?countryCode=BE&apikey='+ apikey, function(data){
    		createTicketmaster(data);
            console.log('Ticketmaster :', self.ticketmaster);
    	});
    	
    }

    self.getEvents();
    self.getTicketmaster();


    self.getVenues = function(events){
        events.forEach(function(event){
            var json = $.getJSON(event.venue_id,function(data){
                event.venue = data
                var json = $.getJSON(event.venue.address_id,function(data2){
                    event.venue.address = data2;
                    var json = $.getJSON(event.user_id,function(data){
                      event.user = data
                      self.events.push(event)
                    })
                })
            })
        })};

        self.defined = function(object){
        	return object != null;
        }
    

    $.put = function(url, data, callback, type){
        if ( $.isFunction(data) ){
            type = type || callback,
            callback = data,
            data = {}
        }
        return $.ajax({
            url: url,
            type: 'PUT',
            success: callback,
            data: data,
            contentType: type
        });
    }

    self.toggleTicket = function(){
        self.showTicketmaster(!self.showTicketmaster());
    }

    self.toggleSpot = function(){
        self.showSpotEvent(!self.showSpotEvent());
    }

    self.showTicketmaster = ko.observable(true);
    self.showSpotEvent = ko.observable(true);

    

    self.getEvents()
    self.getTicketmaster();

}

ko.applyBindings(viewModel);  