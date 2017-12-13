var viewModel = new function()
{
    var self = this;
    self.userName = ko.observable("");
    self.firstName = ko.observable("");
    self.lastName = ko.observable("");
    self.email = ko.observable("");
    self.birthdate = ko.obervable("");
    self.password = ko.password("");

}

ko.applyBindings(viewModel);  