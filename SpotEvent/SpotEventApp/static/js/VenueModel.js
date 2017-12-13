var viewModel = new function()
{
    var self = this;
    self.venueName = ko.observable("");
    self.street = ko.observable("");
    self.number = ko.observable("");
    self.zipCode = ko.observable("");
    self.country = ko.obervable("");

}

ko.applyBindings(viewModel);  