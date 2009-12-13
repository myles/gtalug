/* js-hcalendar. 2007-Feb-01
   (Originally released as JSCalendar on 2005-May-17.)

MIT license:

Copyright (c) 2005 David Glasser

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*/

/* CONFIG */

var dayNames = new Array("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday");
var dayAbbrevs = new Array("S", "M", "T", "W", "T", "F", "S");
var firstDayOfWeek = 0;
var DEBUG = 1;

/* stolen from somebody's blog */

function addLoadEvent(func) {
  var oldonload = window.onload;
  if (typeof window.onload != 'function') {
    window.onload = func;
  } else {
    window.onload = function() {
      oldonload();
      func();
    }
  }
}

/* this function borrowed from prototype.js */
document.getElementsByClassName = function(className) {
  var children = document.getElementsByTagName('*') || document.all;
  var elements = new Array();

  for (var i = 0; i < children.length; i++) {
    var child = children[i];
    if (hasClass(child, className)) {
      elements.push(child);
    }
  }

  return elements;
}

function hasClass (elt, cls) {
  var classNames = elt.className.split(' ');
  for (var j = 0; j < classNames.length; j++) {
    if (classNames[j] == cls) {
      return true;
    }
  }
  return false;
}

function debug(message) {
  if (DEBUG)
    alert(message);
}

var globalDateHash = new Object();

function findHCalendarEvents () {
  if (!(document.getElementById && document.createElement)) {
    debug("No DOM!");
    return;
  }
  var outputDiv = document.getElementById('jhCalendar');
  
  if (outputDiv == null) {
    debug("jhCalendar not found!")
    return;
  }
    
  var events = document.getElementsByClassName("vevent");
  for (var i = 0; i < events.length; i++) {
    processEvent(events[i]);
  }
  

  
  for (year in globalDateHash) {
    for (month in globalDateHash[year]) {
      var mt = makeMonthTable(globalDateHash[year][month], year, month);
      outputDiv.appendChild(mt);
    }
  }
}

function processEvent(ev) {
  var kids = ev.getElementsByTagName('*') || ev.all;
  var eventHash = {};
  var dateInfo;
  for (var i = 0; i < kids.length; i++) {
    var kid = kids[i];
    if (hasClass(kid, 'summary')) {
      eventHash.summary = kid.cloneNode(true); // true means a "deep" cloning
    } else if (hasClass(kid, 'dtstart')) {
      dateInfo = parseDT(kid);
    }
  }
  if (dateInfo == null) {
    debug("didn't find dtstart for " + ev);
    return;
  }
  if (globalDateHash[ dateInfo[0] ] == null)
    globalDateHash[ dateInfo[0] ] = new Object();
  if (globalDateHash[ dateInfo[0] ][ dateInfo[1] ] == null)
    globalDateHash[ dateInfo[0] ][ dateInfo[1] ] = new Object();
  if (globalDateHash[ dateInfo[0] ][ dateInfo[1] ][ dateInfo[2] ] == null)
    globalDateHash[ dateInfo[0] ][ dateInfo[1] ][ dateInfo[2] ] = new Array();
    
  globalDateHash[ dateInfo[0] ][ dateInfo[1] ][ dateInfo[2] ].push(eventHash);
  return;
}

function parseDT(dt) {
  var dtText;
  if (dt.nodeName == 'ABBR' && dt.title) {
    dtText = dt.title;
  } else {
    dtText = dt.firstChild.data;
  }
  var result = dtText.match( /^(\d{4})(\d{2})(\d{2})/ );
  if (result == null) {
    debug("didn't recognize DT: " + dtText);
  }
  
  return [result[1], result[2], result[3]];
}

var monthLength = new Array(31,28,31,30,31,30,31,31,30,31,30,31);

// TODO deal with leap year
getMonthLength = function(year, month) {
  return monthLength[month - 1];
}

function makeMonthTable (monthHash, year, month) {
  currentMonthLength = getMonthLength(year, month);
  
  var today = new Date;
  var todayYear = today.getFullYear();
  var todayMonth = today.getMonth() + 1;
  var todayDay = today.getDate();
    
  var days = new Array(currentMonthLength+1); // We are going to index this array starting at 1.  Because I said so.
  for (var i = 1; i <= currentMonthLength; i++) {
    days[i] = document.createElement('TD');
    days[i].className = 'calDay';
    if (todayYear == year && todayMonth == month && todayDay == i) {
      days[i].className += ' calDayToday';
    }
    var dayLabel = document.createElement('DIV');
    dayLabel.className = 'calDayLabel';
    days[i].appendChild(dayLabel);
    dayLabel.appendChild(document.createTextNode(i));
  }
  
  // populate days here

  for (var day in monthHash) {
    var dayEvents = monthHash[day];
    for (var i = 0; i < dayEvents.length; i++) {
      var eventDiv = document.createElement('DIV');
      eventDiv.className = 'calEvent';
      eventDiv.appendChild(dayEvents[i].summary);
      dayTD = days[day-0];
      dayTD.appendChild(eventDiv);
      if (! hasClass(dayTD, 'calEventDay')) {
        dayTD.className += ' calEventDay';
      }
      
    }
  }
    
  var monthTable = document.createElement('TABLE');
  monthTable.className = 'calTable';
  var tbody = monthTable.appendChild(document.createElement("tbody"));
  var thead = monthTable.appendChild(document.createElement("thead"));
  var tfoot = monthTable.appendChild(document.createElement("tfoot"));
  
  var titleRow = document.createElement('TR');
  // thead.appendChild(titleRow);
  var titleTD = document.createElement('TD');
  titleTD.setAttribute("colspan", 7);
  titleTD.className = 'calHeader';
  
  titleRow.appendChild(titleTD);
  titleTD.appendChild(document.createTextNode(month + "/" + year));
  
  var headerRow = document.createElement('TR');
  headerRow.className = 'calColumnHeader';
  tfoot.appendChild(headerRow);
  thead.appendChild(headerRow);
  for (var i = 0; i <= 6; i++) {
    var headerElement = document.createElement('TD');
    headerElement.className = 'calColumnHeader';
    headerElement.appendChild(document.createTextNode(dayNames[(i+firstDayOfWeek) % 7]));
    headerRow.appendChild(headerElement);
  }
  
  var dateToCheck = new Date();
  dateToCheck.setYear(year);
  dateToCheck.setDate(1);
  dateToCheck.setMonth(month-1);
  var dayOfFirstOfMonth = dateToCheck.getDay();

  var row = tbody.appendChild(document.createElement("TR"));
  // We add 14 (could have gotten away with 7) so that we don't get (-3) % 7 == -3
  for (var i = 0; i < (dayOfFirstOfMonth - firstDayOfWeek + 14) % 7; i++) {
    var emptyDay = document.createElement('TD');
    emptyDay.className = 'calDay calEmptyDay';
    row.appendChild(emptyDay);
  }
  
  for (var i = 1; i <= currentMonthLength; i++) {
    if (row.childNodes.length == 7) {
      row = tbody.appendChild(document.createElement("TR"));
    }
    row.appendChild(days[i]);
  }
  
  while (row.childNodes.length < 7) {
      var emptyDay = document.createElement('TD');
      emptyDay.className = 'calDay calEmptyDay';
      row.appendChild(emptyDay);
  }
  
  return monthTable;
}



addLoadEvent(findHCalendarEvents);