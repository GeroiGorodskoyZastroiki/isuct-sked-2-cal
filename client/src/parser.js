var ics = require('ics').createEvent(event, (error, value) => {
    if (error) {
      console.log(error)
      return
    }
    return value
  })

global.window.createEvents