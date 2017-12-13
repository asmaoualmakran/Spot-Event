var viewModel = new function()
{
    var self = this;
    self.street = ko.observable("");
    self.number = ko.observable("");
    self.zipCode = ko.observable("");
    self.country = ko.observable("");

}

ko.applyBindings(viewModel);  