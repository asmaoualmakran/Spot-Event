var viewModel = new function()
{
    var self = this;
    
    //the search string for the search box
    self.searchstring = ko.observable('');

    //get the user ID from the cookie
    var cookie = document.cookie
    var userID = parseInt(cookie.slice(3));

    //logout the user
    self.logout = function(){
        var json = $.post('/api/logout', ko.toJS(''))
        window.location = 'http://127.0.0.1:8000'
    }

    // the function called by hitting the search button
    self.search = function(){
        window.location.href = "search" + self.searchstring(); 
    }

    // the array which contain the data for the events to be displayed, the event variable contains the Spot-Event events
    self.events = ko.observableArray();

    // puts the data from the get request into the array
    function createEvents(data) {
        self.events(data);
    }

    //the function called when clicking on a Spot-Event event
    self.openEvent = function(id){
        window.location = "http://127.0.0.1:8000/event" + id;
    }

    // filters all the events which are not liked by the user
    self.filterf = function(event){
    	console.log('Like:', event.likedBy)
    	return event.likedBy.includes(userID);
    }
    
    //sorts function to be used on the event array to sort them by date
    self.sortf = function(a, b){
        var aDate = a.event_date;
        var bDate = b.event_date;
        return ((aDate < bDate) ? -1 : ((aDate > bDate) ? 1 : 0));
    }

    // gets the events from the Spot-Event database which need to be displayed
    self.getEvents = function(){
        var json = $.getJSON('/api/event',function(data){
            console.log('Events:',data);
            data.map(el => el.venue = {'address': {'street' : ''}});
            data2 = data.filter(self.filterf);
            console.log('Filtered :',data2);
            data3 = data2.sort(self.sortf);
            console.log('Sorted :', data3);
            self.getVenues(data3);
            console.log('venues added :', self.events());
            //self.getUsers();
            console.log('user added :', self.events());
        });
    }

    // gets the venues, addresses and users for the event data
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
    
    //functions must be executed when starting up the page
    self.getEvents();

}

ko.applyBindings(viewModel);  