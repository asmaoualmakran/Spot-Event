var viewModel = new function()
{
    var self = this;

    // get the user ID from the cookie
    var cookie = document.cookie;
    console.log('cookie :', cookie.slice(3))
    var userID = parseInt(cookie.slice(3));

    //logout the user
    self.logout = function(){
        var json = $.post('/api/logout', ko.toJS(''))
        window.location = 'http://127.0.0.1:8000'
    }

    //the search string for the search box
    self.searchstring = ko.observable('');

    // the function called by hitting the search button
    self.search = function(){
        window.location.href = "search/" + self.searchstring(); 
    }

    //used to store the error response from the server
    self.error = ko.observable();


    //reads the error respond and inserts it in an alert box
    self.failure = function(errors){
        self.error(errors.responseText);
        console.log(self.error());
        var d = document.createElement('DIV');
        d.innerHTML = self.error();
        d.innerHTML = d.innerHTML.replace(/,/g,"<br>")
        d.innerHTML = d.innerHTML.replace('{',"")
        d.innerHTML = d.innerHTML.replace(/"/g," ")
        d.innerHTML = d.innerHTML.replace('}'," ")
        document.getElementById('container').insertBefore(d, document.getElementById('div_1'));
        self.errorsvisible(true);
    }

    // the variable which decides whether or not the error box is visible
    self.errorsvisible=ko.observable(false);


    //store the information about the event
    self.event = {
    	venue_id : ko.observable(),
    	user_id : ko.observable('http://127.0.0.1:8000/api/user/' + userID),
    	event_name : ko.observable(),
    	event_date : ko.observable(),
    	artists : ko.observable(),
    	genre : ko.observable(),
    }

    //stores the information about the venue for the event
    self.venue = {
    	venue_name : ko.observable(),
    	street : ko.observable(),
    	number : ko.observable(),
    	zip_code : ko.observable(),
    	city : ko.observable(),
    	country : ko.observable(),
    }

    // sends a post event to 
    self.addEvent = function(){
    	var Json = $.post('/api/venue', ko.toJS(self.venue),function(data){
    		self.event.venue_id('http://127.0.0.1:8000/api/venue/' + data.id);
    		console.log('Event :',data)
    		var Json2 = $.post('/api/event', ko.toJS(self.event)).fail(function(response){
            self.failure(response);
        });
    	}).fail(function(response){
            self.failure(response);
        });
    	
    };
    
};

ko.applyBindings(viewModel);  