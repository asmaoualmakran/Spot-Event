var viewModel = new function()
{
    var self = this;
    
    self.searchstring = ko.observable('');

    var cookie = document.cookie
    var userID = parseInt(cookie.slice(3));
    var test = 1;

    self.logout = function(){
        var json = $.post('/api/logout', ko.toJS(''))
        window.location = 'http://127.0.0.1:8000'
    }

    self.search = function(){
        window.location.href = "search" + self.searchstring(); 
    }

    self.events = ko.observableArray();

    function createEvents(data) {
        self.events(data);
    }

    self.openEvent = function(id){
        window.location = "http://127.0.0.1:8000/event" + id;
    }

    self.filterf = function(event){
    	console.log('Like:', event.likedBy)
    	return event.likedBy.includes(userID);
    }
    
    self.sortf = function(a, b){
        var aDate = a.event_date;
        var bDate = b.event_date;
        return ((aDate < bDate) ? -1 : ((aDate > bDate) ? 1 : 0));
    }

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
    

    self.getEvents();

}

ko.applyBindings(viewModel);  