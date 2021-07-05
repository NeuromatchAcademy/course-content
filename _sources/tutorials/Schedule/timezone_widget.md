 # Timezone widget

```{div}
<html lang="en">
<head>
<title>Slot selector</title>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
</head>
<body>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.25.3/moment-with-locales.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment-timezone/0.5.28/moment-timezone-with-data-2012-2022.min.js"></script>


<div class="container" style="max-width: 700px;">
    <div class="card" style="margin-top: 50px;">
        <h5 class="card-header">Time slot selector</h5>
        <div class="card-body">

<div>
    <br/>Students and TAs work on <span style = "color:blue"><b>synchronous coursework</b></span>
    and <span style = "color:red"><b>projects</b></span> in times below. (Mentors help in 
 <span style = "color:red">projects</span> time only. )
 See times for coursework and projects in each slot below 
 in your local timezone. <br>
<br>
</div>

<span style = "font-size:13pt; color:green; font-weight:bold"><i> CHOOSE YOUR TIMEZONE:</i></span> <select class="js-Selector" onchange="onChange()" id='timezone'>
</select>
<br><br>
<p><span style = "font-size:13pt;"><i> Course times:</i></span></p>
<div id="times">

</div>

<div>
<br/>People in your timezone often choose the slot in <b>bold</b>,
 but you can choose whichever slot best fits your schedule!
</div>
<div>
    <br>
  * If you have issues with the website please try the Chrome browser.
</div>

<script>
// Adapted from https://matall.in/posts/building-an-usable-timezone-selector/ 

const _t = (s) => {
    if (i18n !== void 0 && i18n[s]) {
      return i18n[s];
    }
  
    return s;
  };
  
  const timezones = [
    "Etc/GMT+12",
    "Pacific/Midway",
    "Pacific/Honolulu",
    "America/Juneau",
    "America/Dawson",
    "America/Boise",
    "America/Chihuahua",
    "America/Phoenix",
    "America/Chicago",
    "America/Regina",
    "America/Mexico_City",
    "America/Belize",
    "America/Detroit",
    "America/Indiana/Indianapolis",
    "America/Bogota",
    "America/Glace_Bay",
    "America/Caracas",
    "America/Santiago",
    "America/St_Johns",
    "America/Sao_Paulo",
    "America/Argentina/Buenos_Aires",
    "America/Godthab",
    "Etc/GMT+2",
    "Atlantic/Azores",
    "Atlantic/Cape_Verde",
    "Europe/London",
    "Africa/Casablanca",
    "Atlantic/Canary",
    "Europe/Belgrade",
    "Europe/Sarajevo",
    "Europe/Brussels",
    "Europe/Amsterdam",
    "Africa/Algiers",
    "Europe/Bucharest",
    "Africa/Cairo",
    "Europe/Helsinki",
    "Europe/Athens",
    "Asia/Jerusalem",
    "Africa/Harare",
    "Europe/Moscow",
    "Asia/Kuwait",
    "Africa/Nairobi",
    "Asia/Baghdad",
    "Asia/Tehran",
    "Asia/Dubai",
    "Asia/Baku",
    "Asia/Kabul",
    "Asia/Yekaterinburg",
    "Asia/Karachi",
    "Asia/Kolkata",
    "Asia/Kathmandu",
    "Asia/Dhaka",
    "Asia/Colombo",
    "Asia/Almaty",
    "Asia/Rangoon",
    "Asia/Bangkok",
    "Asia/Krasnoyarsk",
    "Asia/Shanghai",
    "Asia/Kuala_Lumpur",
    "Asia/Taipei",
    "Australia/Perth",
    "Asia/Irkutsk",
    "Asia/Seoul",
    "Asia/Tokyo",
    "Asia/Yakutsk",
    "Australia/Darwin",
    "Australia/Adelaide",
    "Australia/Sydney",
    "Australia/Brisbane",
    "Australia/Hobart",
    "Asia/Vladivostok",
    "Pacific/Guam",
    "Asia/Magadan",
    "Pacific/Fiji",
    "Pacific/Auckland",
    "Pacific/Tongatapu"
  ];
  
  const i18n = {
    "Etc/GMT+12": "International Date Line West",
    "Pacific/Midway": "Midway Island, Samoa",
    "Pacific/Honolulu": "Hawaii",
    "America/Juneau": "Alaska",
    "America/Dawson": "Pacific Time (US and Canada); Tijuana",
    "America/Boise": "Mountain Time (US and Canada)",
    "America/Chihuahua": "Chihuahua, La Paz, Mazatlan",
    "America/Phoenix": "Arizona",
    "America/Chicago": "Central Time (US and Canada)",
    "America/Regina": "Saskatchewan",
    "America/Mexico_City": "Guadalajara, Mexico City, Monterrey",
    "America/Belize": "Central America",
    "America/Detroit": "Eastern Time (US and Canada)",
    "America/Indiana/Indianapolis": "Indiana (East)",
    "America/Bogota": "Bogota, Lima, Quito",
    "America/Glace_Bay": "Atlantic Time (Canada)",
    "America/Caracas": "Caracas, La Paz",
    "America/Santiago": "Santiago",
    "America/St_Johns": "Newfoundland and Labrador",
    "America/Sao_Paulo": "Brasilia",
    "America/Argentina/Buenos_Aires": "Buenos Aires, Georgetown",
    "America/Godthab": "Greenland",
    "Etc/GMT+2": "Mid-Atlantic",
    "Atlantic/Azores": "Azores",
    "Atlantic/Cape_Verde": "Cape Verde Islands",
    "Europe/London": "Dublin, Edinburgh, Lisbon, London",
    "Africa/Casablanca": "Casablanca, Monrovia",
    "Atlantic/Canary": "Canary Islands",
    "Europe/Belgrade": "Belgrade, Bratislava, Budapest, Ljubljana, Prague",
    "Europe/Sarajevo": "Sarajevo, Skopje, Warsaw, Zagreb",
    "Europe/Brussels": "Brussels, Copenhagen, Madrid, Paris",
    "Europe/Amsterdam": "Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna",
    "Africa/Algiers": "West Central Africa",
    "Europe/Bucharest": "Bucharest",
    "Africa/Cairo": "Cairo",
    "Europe/Helsinki": "Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius",
    "Europe/Athens": "Athens, Istanbul, Minsk",
    "Asia/Jerusalem": "Jerusalem",
    "Africa/Harare": "Harare, Pretoria",
    "Europe/Moscow": "Moscow, St. Petersburg, Volgograd",
    "Asia/Kuwait": "Kuwait, Riyadh",
    "Africa/Nairobi": "Nairobi",
    "Asia/Baghdad": "Baghdad",
    "Asia/Tehran": "Tehran",
    "Asia/Dubai": "Abu Dhabi, Muscat",
    "Asia/Baku": "Baku, Tbilisi, Yerevan",
    "Asia/Kabul": "Kabul",
    "Asia/Yekaterinburg": "Ekaterinburg",
    "Asia/Karachi": "Islamabad, Karachi, Tashkent",
    "Asia/Kolkata": "Chennai, Kolkata, Mumbai, New Delhi",
    "Asia/Kathmandu": "Kathmandu",
    "Asia/Dhaka": "Astana, Dhaka",
    "Asia/Colombo": "Sri Jayawardenepura",
    "Asia/Almaty": "Almaty, Novosibirsk",
    "Asia/Rangoon": "Yangon Rangoon",
    "Asia/Bangkok": "Bangkok, Hanoi, Jakarta",
    "Asia/Krasnoyarsk": "Krasnoyarsk",
    "Asia/Shanghai": "Beijing, Chongqing, Hong Kong SAR, Urumqi",
    "Asia/Kuala_Lumpur": "Kuala Lumpur, Singapore",
    "Asia/Taipei": "Taipei",
    "Australia/Perth": "Perth",
    "Asia/Irkutsk": "Irkutsk, Ulaanbaatar",
    "Asia/Seoul": "Seoul",
    "Asia/Tokyo": "Osaka, Sapporo, Tokyo",
    "Asia/Yakutsk": "Yakutsk",
    "Australia/Darwin": "Darwin",
    "Australia/Adelaide": "Adelaide",
    "Australia/Sydney": "Canberra, Melbourne, Sydney",
    "Australia/Brisbane": "Brisbane",
    "Australia/Hobart": "Hobart",
    "Asia/Vladivostok": "Vladivostok",
    "Pacific/Guam": "Guam, Port Moresby",
    "Asia/Magadan": "Magadan, Solomon Islands, New Caledonia",
    "Pacific/Fiji": "Fiji Islands, Kamchatka, Marshall Islands",
    "Pacific/Auckland": "Auckland, Wellington",
    "Pacific/Tongatapu": "Nuku'alofa"
  }
  
  const selectorOptions = moment.tz.names()
    .filter(tz => {
      return timezones.includes(tz)
    })
    .reduce((memo, tz) => {
      memo.push({
        name: tz,
        offset: moment.tz(tz).utcOffset()
      });
      
      return memo;
    }, [])
    .sort((a, b) => {
      return a.offset - b.offset
    })
    .reduce((memo, tz) => {
      const timezone = tz.offset ? moment.tz(tz.name).format('Z') : '';
  
      return memo.concat(`<option value="${tz.name}">(GMT${timezone}) ${_t(tz.name)}</option>`);
    }, "");
    
  document.querySelector(".js-Selector").innerHTML = selectorOptions;
  
  /*
  $(".js-Selector").on("change", e => {
    const timestamp = dateTimeUtc.unix();
    const offset = moment.tz(e.target.value).utcOffset() * 60;
    const dateTimeLocal = moment.unix(timestamp + offset).utc();
  
    document.querySelector(".js-TimeLocal").innerHTML = dateTimeLocal.format("ddd, DD MMM YYYY HH:mm:ss");
  });
  */
  
  document.querySelector(".js-Selector").value = "";
  
  function formatTime(time) {
      if(time == '00:00') {
        return '00:00 (midnight)';
    } else if(time == '12:00') {
        return '12:00 (noon)';
    } else {
        if(time > '12:00') {
            return time + " (" + (Number(time.substr(0, 2)) - 12) + ':' + (time.substr(3, 2) + 'PM') + ")";
        } else {
            return time;
        }
    }
  }
  
  function onChange() {
    var startTimes0 = {'1': ['00:30', '09:00'],
                      '2': ['04:00', '12:30'],
                      '3': ['07:30', '16:00'],
                      '4': ['14:00', '22:30'],
                      '5': ['17:30', '02:00']}
    
    var startTimes = {'1': ['00:30', '05:00'],
                        '2': ['07:30', '12:00'],
                        '3': ['07:30', '12:00'],
                        '4': ['17:30', '22:00'],
                        '5': ['17:30', '22:00']}

    var startTimes2 = {'1': ['06:00', '09:00'],
                        '2': ['04:00', '07:00'],
                        '3': ['13:00', '16:00'],
                        '4': ['14:00', '17:00'],
                        '5': ['23:00', '02:00']}
    
    var regions = {'1': 'Eastern Asia / Australia',
                   '2': 'Middle East / India',
                   '3': 'Europe / Africa',
                   '4': 'Eastern Americas',
                   '5': 'Western Americas'}

    

      var deltas = []
      for(var prop in startTimes0) {
        var startTime0 = moment.tz("2021-07-13 " + startTimes0[prop][0], "UTC").clone().tz(document.getElementById('timezone').value).format().substr(11, 5);
      var fracHour = Number(startTime0.substr(0, 2)) + Number(startTime0.substr(3, 2)) / 60.0;
      deltas.push(Math.abs(fracHour - 8.6));
    }
    var bestDelta = deltas.indexOf(Math.min.apply(Math, deltas));
  
  
    var theStr = "<p>";
    var i = 0;
    for(var prop in startTimes) {
        var startTime = moment.tz("2021-07-13 " + startTimes[prop][0], "UTC").clone().tz(document.getElementById('timezone').value).format().substr(11, 5);
        var endTime = moment.tz("2021-07-13 " + startTimes[prop][1], "UTC").clone().tz(document.getElementById('timezone').value).format().substr(11, 5);
        
        var startTime2 = moment.tz("2021-07-13 " + startTimes2[prop][0], "UTC").clone().tz(document.getElementById('timezone').value).format().substr(11, 5);
        var endTime2 = moment.tz("2021-07-13 " + startTimes2[prop][1], "UTC").clone().tz(document.getElementById('timezone').value).format().substr(11, 5);
        

      var bold = false;
        if( bestDelta == i) {
          bold = true;
        theStr += "<b>"
      }
      theStr += "<u>SLOT " + prop + " (daytime in " + regions[prop] + ") <br>"
        if(bestDelta == i) {
          wasBold = true;
          theStr += "</b>"
      }
      else {
          theStr += ""
      }
      if(prop.valueOf() === new String("2").valueOf() || prop.valueOf() === new String("4").valueOf()){
        theStr += "</u> projects are " + 
                '<span style = "color:red;font-family:monospace;font-size:12pt;">' + formatTime(startTime2) + " - " + 
                  formatTime(endTime2)+'</span> local time;';
        theStr += "<br> coursework is " + 
                '<span style = "color:blue;font-family:monospace;font-size:12pt;">' + formatTime(startTime) + " - " + 
                  formatTime(endTime)+'</span> local time;';
    }
    else {    
    theStr += "</u> coursework is " + 
                '<span style = "color:blue;font-family:monospace;font-size:12pt;">' + formatTime(startTime) + " - " + 
                  formatTime(endTime)+'</span> local time;';
      theStr += "<br> projects are " + 
                '<span style = "color:red;font-family:monospace;font-size:12pt;">' + formatTime(startTime2) + " - " + 
                  formatTime(endTime2)+'</span> local time;';
                }
                
    theStr += "</p>"
      i++;
    }
    document.getElementById('times').innerHTML = theStr;
  }
  
  onChange();

</script>
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

</div>
</div>
</div>
</body></html>
```
