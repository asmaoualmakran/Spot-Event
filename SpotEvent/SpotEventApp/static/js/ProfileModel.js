
var viewModel = new function()
{
    var self = this;

    self.searchstring = ko.observable('');

    self.search = function(){
        window.location.href = "search" + self.searchstring(); 
    }

   var cookie = document.cookie
   var userID = parseInt(cookie.slice(3));
    console.log('ID :',userID);

    self.profile = {
        username : ko.observable(),
        first_name : ko.observable(),
        last_name : ko.observable(),
        email : ko.observable(),
        birthday : ko.observable(),
        address_id : ko.observable(),
        id : ko.observable()
    }

    self.profile2 = {
        street : ko.observable(),
        number : ko.observable(),
        zip_code : ko.observable(),
        city : ko.observable(),
        country : ko.observable()
    }

    
    function createProfile(data){
        self.profile.username(data.username);
        self.profile.first_name(data.first_name);
        self.profile.last_name(data.last_name);
        self.profile.email(data.email);
        self.profile.birthday(data.birthday);
        self.profile.address_id(data.address_id);
        self.profile.id(data.id);
    }

    function createProfile2(data){
        self.profile2.street(data.street);
        self.profile2.number(data.number);
        self.profile2.zip_code(data.zip_code);
        self.profile2.city(data.city);
        self.profile2.country(data.country);
    }

    self.getProfile = function(){
    	console.log('getProfile');
    	var json = $.getJSON('/api/user/'+ userID,function(data){
            console.log('Profile :',data);
            createProfile(data);
            self.getAddress();
            console.log(self.profile.username)
        });
    }

    self.getAddress = function(){
        var json = $.getJSON(self.profile.address_id(),function(data2){
            console.log('Address :',data2);
            createProfile2(data2);
        });
    }

    self.getProfile();


    self.saveProfile = function(){
        console.log('saveProfile')
        var JsonData = ko.toJSON(self.profile);
        console.log(JsonData);
        $.put('/api/user/1', ko.toJSON(self.profile))
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

}

ko.applyBindings(viewModel);  