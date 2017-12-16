
var viewModel = new function()
{
    var self = this;
    

    self.data = {
    userNameR : ko.observable(),
    firstName : ko.observable(),
    lastName : ko.observable(),
    email : ko.observable(),
    birthdate : ko.observable(),
    passwordR : ko.observable(),
    }

    self.data2 = {
        userNameL : ko.observable(),
        passwordL : ko.observable(),
    }

    self.submit = function(){
    	console.log("submit")
    	$.post('/api/people',function(){console.log("Succes")},
    		function() { console.log("Failure")},self.data)
    };

}

ko.applyBindings(viewModel);  