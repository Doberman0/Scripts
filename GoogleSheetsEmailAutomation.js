function CheckSales() {
  // The following values refer to the column number-1 in the spreadsheet
  var email = 0;
  var name = 1;
  var lastname = 2;
  var time = 3;
  
  // Email subject
  var subject = 'Interview';

  // Load the sheet
  var sheet = SpreadsheetApp.getActive().getSheetByName("Recipients");
  var data = sheet.getDataRange().getDisplayValues();
  
  // Sending each of the emails out
  data.slice(1).forEach(function(row) { 
    // Compose the message
    var message = 'Hi ' + row[name] + '\nYou have an interview appointment at ' + row[time] + '.\nBest of luck! \nThe team'; 

    //Send the message off
    MailApp.sendEmail(row[email], subject, message);
    //Logger.log(message);
  }); 
}
