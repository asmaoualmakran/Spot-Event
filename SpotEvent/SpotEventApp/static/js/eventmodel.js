
var viewModel = new function()
{
    var self = this;

     //the search string for the search box
    self.searchstring = ko.observable('');

    // the function called by hitting the search button
    self.search = function(){
        window.location.href = "search" + self.searchstring(); 
    }

    //get the user ID from the cookie
    var cookie = document.cookie
    var userID = parseInt(cookie.slice(3));
    console.log('ID :',userID);

    //logout the user
    self.logout = function(){
        var json = $.post('/api/logout', ko.toJS(''))
        window.location = 'http://127.0.0.1:8000'
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
    self.errorsvisible = ko.observable(false);


    //gets the event ID from the url
    var url = window.location.href;
    var eventID = url.slice(27);
    console.log('ID :', eventID)

    //the data required to add a new review
    self.addReview = {
        score : ko.observable(),
        review: ko.observable(),
        user_id : ko.observable(),
        venue_id : ko.observable()
    }

    // the data for the event
    self.event = {
        venue_id : ko.observable(),
        user_id : ko.observable(),
        event_name : ko.observable(),
        event_date : ko.observable(),
        artists : ko.observable(),
        genre : ko.observable(),
    }

    //the data for the user which created  the event
    self.user = {
        username : ko.observable(),
        email : ko.observable(),
    }

    //the data for the venue of the event
    self.venue = {
        address_id : ko.observable(),
        venue_name : ko.observable(),
    }

    //the data for the address of the venue of the event
    self.address = {
        street : ko.observable(),
        number : ko.observable(),
        zip_code : ko.observable(),
        city : ko.observable(),
        country : ko.observable(),
    }

    //the data for a single review
    self.review = {
        user_id : ko.observable(),
        score : ko.observable(),
        review : ko.observable()
    }

    // an array which contains all the review of the venue of an event
    self.reviews = ko.observableArray();

    //creates the review from the data
    function createReview(data) {
        self.review.user_id(data.user_id);
        self.review.score(data.score);
        self.review.review(data.review);
    }

    // puts the reviews in the array
    function createReviews(data) {
        self.reviews(data)
    }

    //creates the event data
    function createEvent(data) {
        self.event.venue_id(data.venue_id);
        self.event.user_id(data.user_id);
        self.event.event_name(data.event_name);
        self.event.event_date(data.event_date);
        self.event.artists(data.artists);
        self.event.genre(data.genre);
    }

    //creates the user data
    function createUser(data) {
        self.user.username(data.username);
        self.user.email(data.email);
    }

    //creates the address data
    function createAddress(data) {
        self.address.street(data.street);
        self.address.number(data.number);
        self.address.zip_code(data.zip_code);
        self.address.city(data.city);
        self.address.country(data.country);
    }

    //creates the venue data
    function createVenue(data) {
        self.venue.venue_name(data.venue_name);
        self.venue.address_id(data.address_id);
    }

    //gets the event data from the database
    self.getEvent = function(){
        console.log('getEvent');
        var json = $.getJSON('/api/event/'+eventID, function(data){
            console.log('Event :', data);
            createEvent(data);
            self.addReview.venue_id(data.venue_id);
            self.getUser();
            self.getVenue();
            self.getReviews();
        })
    }

    //gets the venue data from the database
    self.getVenue = function(){
        console.log('getVenue');
        var json = $.getJSON(self.event.venue_id(),function(data){
            console.log('Profile :',data);
            createVenue(data);
            self.getAddress();
        });
    }

    // gets the user data form the database
    self.getUser = function(){
        console.log('getUser');
        var json = $.getJSON(self.event.user_id(),function(data){
            console.log('User :', data);
            createUser(data);
        })
    }

    //gets the address data from the database
    self.getAddress = function(){
        var json = $.getJSON(self.venue.address_id(),function(data){
            console.log('Address :',data);
            createAddress(data);
            initialize();
            codeAddress();
        });
    }

    // the filter which selects the correct reviews for the event
    self.filterf = function(review){
        return review.venue_id == self.event.venue_id();
    }

    // gets the reviews for the event from the database
    self.getReviews = function(){
        var json = $.getJSON('/api/review',function(data){
            console.log('Reviews :',data);
            data2 = data.filter(self.filterf);
            console.log('Filtered :',data2);
            createReviews(data2);
        });
    }

    // the variables which decides whether or not the reviews are visible and whether or not the addreview box is visible
    self.reviewsVisible = ko.observable(false);
    self.addReviewVisible = ko.observable(false);

    // makes the reviews visible (called by the button)
    self.openReviews = function(){
        self.reviewsVisible(true);
        console.log(self.reviewsVisible)
    }

    // makes the reviews invisible (called by the button)
    self.closeReviews = function(){
        self.reviewsVisible(false);
        console.log(self.reviewsVisible)
    }  

    //make the addreview box visible or invisible (called by the button)
    self.openAddReview = function(){
        self.addReviewVisible(!self.addReviewVisible());
    }

    // posts a new review to the database
    self.addRev = function(){
        console.log('Review :', self.addReview);
        var json = $.post('/api/review',ko.toJS(self.addReview),function(data){
            console.log('reviewresponse :',data)
            self.getReviews();
            //self.addReview.score('');
            //self.addReview.reviewText('');
        }).fail(function(response){
            self.failure(response);
        })
    }

    // the function called when an event is liked, this is a put request
    self.likeEvent = function(){
        var json = $.put('api/eventlike/' + eventID + '/' + userID);
    }


    // calls the function to get the event
    self.getEvent();
    
    //initializes the google map
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

    // codes the address and marks it on the map
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

    // since jquery didnt have a put function we created one
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
}

ko.applyBindings(viewModel);  