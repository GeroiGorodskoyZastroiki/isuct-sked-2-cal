<script setup>
const props = defineProps(['schedule'])
const emit = defineEmits(['schedule'])

let scheduleWithNicks = props.schedule
let subjects = [...new Set(getSubjects())]
let nicks = {}

function getSubjects() {
  let temp = []
  for (let i = 0; i < props.schedule.length; i++) {
    temp.push(props.schedule[i]['subject'])
  }
  return temp
}

function setNick(event) {
  let actualName = event.target.parentElement.children[0].textContent
  let nick = event.target.parentElement.children[1].value
  if (actualName == nick) return
  nicks[actualName] = nick
}

function changeNames() {
  for (let i = 0; i < scheduleWithNicks.length; i++) {
    if (scheduleWithNicks[i]['subject'] in nicks) {
      scheduleWithNicks[i]['subject'] = nicks[scheduleWithNicks[i]['subject']]
    }
  }
  emit('schedule', scheduleWithNicks)
}
</script>

<template>
    <pre>
        Можете задать каждому предмету псевдоним
        (Например: Большие Данные - Big Data)
    </pre>
    <div v-for="value in subjects" class="grid" @change="setNick($event)">
      <div class="div-border">{{ value }}</div>
      <input class="div-border nick" placeholder="—">
    </div>
    <button @click='changeNames'>Далее</button>
</template>

<style scoped>
</style>