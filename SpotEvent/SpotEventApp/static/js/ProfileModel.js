
var viewModel = new function()
{
    var self = this;

    self.dummy = {
    	userName : 'Thoraxis',
    	firstName : 'Robin',
    	lastName : 'Cortvrindt',
    	email : 'cortvrindt.robin@gmail.com',
    	birthdate : '28/11/95',
    	password : '*********',
    }

    self.userName = ko.observable(self.dummy.userName);
    self.firstName = ko.observable(self.dummy.firstName);
    self.lastName = ko.observable(self.dummy.lastName);
    self.email = ko.observable(self.dummy.email);
    self.birthdate = ko.observable(self.dummy.birthdate);
    self.password = ko.observable(self.dummy.password);
    
    self.data;

    self.getProfile = function(){
    	console.log('getProfile')
    	$.get('TODO : get profile', self.data)
    }

    self.saveProfile = function(){
        console.log('saveProfile')
        $.post('TODO: post profile', self.data)
    }

}

ko.applyBindings(viewModel);  