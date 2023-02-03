<script setup>
import { onMounted } from 'vue'
import { createEvents } from 'ics'
const props = defineProps(['schedule'])

onMounted(() => {
  createButton()
})

function createButton() {
    let blob = new Blob([createCalendar()], {type: 'text/plain'})
    let href = URL.createObjectURL(blob)
    let button = '<a href="'+ href +'" download="cal.ics"><button>Загрузить</button></a>'

    let downloadDiv = document.getElementsByClassName('download')[0]
    downloadDiv.innerHTML = button
}

function createCalendar() {
    let allPairs = []

    for (let i = 0; i < props.schedule.length; i++) {
        let startDay = props.schedule[i]['date']['start'].split('.')
        let endDay = props.schedule[i]['date']['end'].split('.')
        let startTime = props.schedule[i]['time']['start'].split(':')
        let endTime = props.schedule[i]['time']['end'].split(':')
        let weekDay = props.schedule[i]['date']['weekday']
        let byDay = ['MO','TU','WE','TH','FR','SA','SU']
        let until = endDay[2]+endDay[1]+endDay[0]+'T000000Z'
        console.log(byDay[weekDay-1])
        console.log(until)
        console.log(`FREQ=WEEKLY;BYDAY=${byDay[weekDay-1]};INTERVAL=1;UNTIL=${until}`)
        console.log([startDay[2], startDay[1], startDay[0], startTime[0], startTime[1]])
        console.log([startDay[2], startDay[1], startDay[0], endTime[0], endTime[1]])
        var event = {
            start: [Number(startDay[2]), Number(startDay[1]), Number(startDay[0]), Number(startTime[0]), Number(startTime[1])],
            end: [Number(startDay[2]), Number(startDay[1]), Number(startDay[0]), Number(endTime[0]), Number(endTime[1])],
            title: props.schedule[i]['name'],
            recurrenceRule: `FREQ=WEEKLY;BYDAY=${byDay[weekDay-1]};INTERVAL=1;UNTIL=${until}`
        }
        allPairs.push(event)
    }
    return createEvents(allPairs).value
}
</script>

<template>
    <pre>
        Готово!
        Загрузите файл календаря
    </pre>
    <div class="download"></div>
</template>

<style scoped>
</style>