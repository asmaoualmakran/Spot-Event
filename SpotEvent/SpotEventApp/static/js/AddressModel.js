
var viewModel = new function()
{
    var self = this;

    self.event = {
        venue_id : ko.observable(),
        user_id : ko.observable(),
        event_name : ko.observable(),
        event_date : ko.observable(),
        artists : ko.observable(),
        genre : ko.observable(),
    }

    self.user = {
        username : ko.observable(),
        email : ko.observable(),
    }

    self.venue = {
        address_id : ko.observable(),
        venue_name : ko.observable(),
    }

    self.address = {
        street : ko.observable(),
        number : ko.observable(),
        zip_code : ko.observable(),
        city : ko.observable(),
        country : ko.observable(),
    }

    self.review = {
        user_id : ko.observable(),
        score : ko.observable(),
        review : ko.observable()
    }

    self.reviews = ko.observableArray();

    function createReview(data) {
        self.review.user_id(data.user_id);
        self.review.score(data.score);
        self.review.review(data.review);
    }

    function createReviews(data) {
        self.reviews(data)
    }

    function createEvent(data) {
        self.event.venue_id(data.venue_id);
        self.event.user_id(data.user_id);
        self.event.event_name(data.event_name);
        self.event.event_date(data.event_date);
        self.event.artists(data.artists);
        self.event.genre(data.genre);
    }

    function createUser(data) {
        self.user.username(data.username);
        self.user.email(data.email);
    }

    function createAddress(data) {
        self.address.street(data.street);
        self.address.number(data.number);
        self.address.zip_code(data.zip_code);
        self.address.city(data.city);
        self.address.country(data.country);
    }

    function createVenue(data) {
        self.venue.venue_name(data.venue_name);
        self.venue.address_id(data.address_id);
    }

    self.getEvent = function(){
        console.log('getEvent');
        var json = $.getJSON('/api/event/1', function(data){
            console.log('Event :', data);
            createEvent(data);
            self.getUser();
            self.getVenue();
        })
    }

    self.getVenue = function(){
        console.log('getVenue');
        var json = $.getJSON(self.event.venue_id(),function(data){
            console.log('Profile :',data);
            createVenue(data);
            self.getAddress();
        });
    }

    self.getUser = function(){
        console.log('getUser');
        var json = $.getJSON(self.event.user_id(),function(data){
            console.log('User :', data);
            createUser(data);
        })
    }


    self.getAddress = function(){
        var json = $.getJSON(self.venue.address_id(),function(data){
            console.log('Address :',data);
            createAddress(data);
        });
    }

    self.filterf = function(review){
        return review.venue_id == self.event.venue_id();
    }

    self.getReviews = function(){
        var json = $.getJSON('/api/review',function(data){
            console.log('Reviews :',data);
            data2 = data.filter(self.filterf);
            console.log('Filtered :',data2);
            createReviews(data2);
        });
    }

    self.reviewsVisible = ko.observable(false);

    self.openReviews = function(){
        self.reviewsVisible(true);
        console.log(self.reviewsVisible)
    }

    self.closeReviews = function(){
        self.reviewsVisible(false);
        console.log(self.reviewsVisible)
    }


    self.getEvent();
    self.getReviews();

}

ko.applyBindings(viewModel);  