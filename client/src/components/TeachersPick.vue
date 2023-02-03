<script setup>
const props = defineProps(['schedule'])
const emit = defineEmits(['schedule'])

let scheduleWithPropTeachers = props.schedule
let subjectsAndTeachers = getSubjects()
let teachers = [...new Set(subjectsAndTeachers[1])]
let subjects = [...new Set(subjectsAndTeachers[0])]
let types = JSON.parse(JSON.stringify(subjects))
for (let i = 0; i < types.length; i++) {
  types[i] = types[i].split(' / ')[1]
  subjects[i] = subjects[i].split(' / ')[0]
}
// console.log(subjects)
// console.log(teachers)

function getSubjects() { // НЕ РАБОТАЕТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТТ
  //console.log(props.schedule)
  let subjects = []
  let teachers = []
  for (let i = 0; i < props.schedule.length; i++) {
    if (props.schedule[i]['teachers'].length > 1) {
      let teachersForSubject = []
      for (let j = 0; j < props.schedule[i]['teachers'].length; j++) {
        if (props.schedule[i]['teachers'][j]['name'] == '—') break
        else teachersForSubject.push(props.schedule[i]['teachers'][j]['name'])
      }
      if (teachersForSubject.length > 1) {
        subjects.push(props.schedule[i]['subject'] + ' / ' + props.schedule[i]['type'])
        teachers.push(teachersForSubject)
      }
    }
  }
  return [subjects, teachers]
}

function changeTeacherState(event) {
  //console.log(event)
  if (event.target.classList.contains('crossed')) {
    event.target.classList.remove('crossed')
    let index = subjects.findIndex(x => x == event.path[2].children[0].textContent.split(' / ')[0])
    teachers[index].push(event.target.textContent)
  }
  else {
    event.target.classList.add('crossed')
    let index = subjects.findIndex(x => x == event.path[2].children[0].textContent.split(' / ')[0])
    teachers[index].splice(teachers[index].findIndex(x => x == event.target.textContent), 1)
  }
}

function setTeachers() {
  for (let i = 0; i < scheduleWithPropTeachers.length; i++) {
    for (let j = 0; j < subjects.length; j++) {
      if ((scheduleWithPropTeachers[i]['subject'] == subjects[j]) && (scheduleWithPropTeachers[i]['type'] == types[j])) {
        scheduleWithPropTeachers[i]['teachers'] = teachers[j]
      }
    }
  }
  emit('schedule', scheduleWithPropTeachers)
}
</script>

<template>
    <pre>
        Исключите не своих преподавателей для каждого предмета

        (Если ваши преподаватели действительно меняются, то можете не исключать их, тогда в расписании будет значится 2 ФИО)
    </pre>
    <div v-for="value, key in subjects" class="grid">
      <div class="div-border">{{ value + ' / ' + types[key] }}</div>
      <div class="options">
        <button v-for="value in teachers[key]" @click="changeTeacherState($event)" class="newbutton">
          {{ value }}
        </button>
      </div>
    </div>
    <button @click='setTeachers'>Далее</button>
</template>

<style scoped>
</style>