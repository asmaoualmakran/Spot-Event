
var viewModel = new function()
{
    var self = this;

    self.searchstring = ko.observable('');

    self.search = function(){
        window.location.href = "search/" + self.searchstring(); 
    }

    var url = window.location.href;
    var eventID = url.slice(28);
    console.log('ID :', eventID)

    self.addReview = {
        score : ko.observable(),
        review: ko.observable(),
        user_id : ko.observable(),
        venue_id : ko.observable()
    }

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
        var json = $.getJSON('/api/event/'+eventID, function(data){
            console.log('Event :', data);
            createEvent(data);
            self.addReview.venue_id(data.venue_id);
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
            initialize();
            codeAddress();
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
    self.addReviewVisible = ko.observable(false);

    self.openReviews = function(){
        self.reviewsVisible(true);
        console.log(self.reviewsVisible)
    }

    self.closeReviews = function(){
        self.reviewsVisible(false);
        console.log(self.reviewsVisible)
    }

    self.openAddReview = function(){
        self.addReviewVisible(!self.addReviewVisible());
    }

    self.addRev = function(){
        console.log('Review :', self.addReview);
        var json = $.post('/api/review',ko.toJS(self.addReview),function(data){
            console.log('reviewresponse :',data)
            self.getReviews();
            //self.addReview.score('');
            //self.addReview.reviewText('');
        })
    }


    self.getEvent();
    self.getReviews();

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