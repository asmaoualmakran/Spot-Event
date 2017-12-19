
var viewModel = new function()
{
    var self = this;
    

    self.data = {
    username : ko.observable('Thoraxis'),
    first_name : ko.observable('Robin'),
    last_name : ko.observable('Cortvrindt'),
    email : ko.observable('cortvrindt.robin@gmail.com'),
    birthday : ko.observable('1995-11-28'),
    password : ko.observable('password'),
    street : ko.observable('Vijverstraat'),
    number : ko.observable('27'),
    city : ko.observable('Asse'),
    zip_code : ko.observable('1730'),
    country : ko.observable('Belgium'),
    }


    self.data2 = {
        email : ko.observable("test@tester.com"),
        password : ko.observable("password"),
    }




    self.register = function(){
    	console.log("Register :",self.data,ko.toJSON(self.data))
    	$.post('/api/user',ko.toJSON(self.data))
    };

    self.login = function(){
        console.log(ko.toJSON(self.data2))
        var JsonData = ko.toJSON(self.data2);
        console.log(self.data2)
        $.post('/api/user/authenticate',JsonData)
    };



}

ko.applyBindings(viewModel);  