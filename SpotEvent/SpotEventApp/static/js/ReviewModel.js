var viewModel = new function()
{
    var self = this;
    self.userNameR = ko.observable("");
    self.firstName = ko.observable("");
    self.lastName = ko.observable("");
    self.email = ko.observable("");
    self.birthdate = ko.obervable("");
    self.passwordR = ko.password("");
    
    self.userNameL = ko.observable("");
    self.passwordL = ko.observable("");

}

ko.applyBindings(viewModel);  