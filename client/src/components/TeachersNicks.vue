<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue'
import { allTeachersSaved } from './teachers';
const props = defineProps(['schedule'])
const emit = defineEmits(['schedule'])

let scheduleWithNicks = props.schedule
let allTeachers = []
allTeachers = allTeachersSaved
//getAllTeachers()
let teachers = [...new Set(getTeachers())]
let fullNames = ref(Array(teachers.length).fill(''))

onMounted(() => {
  setNewNames()
})

function getTeachers() {
  //console.log(props.schedule)
  let temp = []
  for (let i = 0; i < props.schedule.length; i++) {
    for (let j = 0; j < props.schedule[i]['teachers'].length; j++) {
      if (props.schedule[i]['teachers'][j]['name'] != '') temp.push(props.schedule[i]['teachers'][j]['name'])
    }
  }
  //console.log(temp)
  return temp
}

function getAllTeachers() {
  function makeHttpObject() {
      try {return new XMLHttpRequest();}
      catch (error) {}
      try {return new ActiveXObject("Msxml2.XMLHTTP");}
      catch (error) {}
      try {return new ActiveXObject("Microsoft.XMLHTTP");}
      catch (error) {}
      throw new Error("Could not create HTTP request object.")
  }

  var request = makeHttpObject();
  request.open("GET", "http://localhost:8080/https://www.isuct.ru/sveden/employees", true);
  request.send(null);
  request.onreadystatechange = function() {
      if (request.readyState == 4) {
          allTeachers = [...new Set(Array.from(request.responseText.matchAll(/<td itemprop="fio">.*<\/td>/g), x => x[0]))]
          for (let i = 0; i < allTeachers.length; i++) {
              allTeachers[i] = allTeachers[i].replace('<td itemprop="fio">', '').replace('</td>', '').replace('  ', ' ').split(' ')
          }
          allTeachers.splice(0,1)
          console.log(allTeachers)
          setNewNames()
      }
  }
}

function setNewNames() {
  let names = document.getElementsByClassName('name')
  for (let i = 0; i < names.length; i++) {
      let surnameAndInitials = names[i].innerHTML.split(' ')
      let surname = surnameAndInitials[0]
      let nameInitial = surnameAndInitials[1].split('.')[0]
      let patronymicInitial = surnameAndInitials[1].split('.')[1]

      for (let j = 0; j < allTeachers.length; j++) {
        if (allTeachers[j][0] == surname) {
          let FIO = allTeachers[j][0] + ' ' + allTeachers[j][1] + ' ' + allTeachers[j][2]
          fullNames.value[i] = FIO
          break
        }
      }
      if (fullNames.value[i] == '') fullNames.value[i] = names[i].innerHTML
  }
}

function setName(variant) {
  switch (variant) {
    case 0:
    for (let i = 0; i < scheduleWithNicks.length; i++) {
        for (let j = 0; j < scheduleWithNicks[i]['teachers'].length; j++) {
          for (let k = 0; k < teachers.length; k++) {
            if (teachers[k] == scheduleWithNicks[i]['teachers'][j]['name']) {
              if (fullNames.value[k].length == 0) {
                scheduleWithNicks[i]['teachers'][j]['name'] = fullNames.value[k]
              }
            }
          }
        }
      }
      break;
    case 1:
      for (let i = 0; i < scheduleWithNicks.length; i++) {
        for (let j = 0; j < scheduleWithNicks[i]['teachers'].length; j++) {
          for (let k = 0; k < teachers.length; k++) {
            if (teachers[k] == scheduleWithNicks[i]['teachers'][j]['name']) {
              if (fullNames.value[k].split(' ').length == 3) {
                let splittedFIO = fullNames.value[k].split(' ')
                let newName = splittedFIO[0] + ' ' + splittedFIO[1] + ' ' + splittedFIO[2]
                scheduleWithNicks[i]['teachers'][j]['name'] = newName
              }
              else scheduleWithNicks[i]['teachers'][j]['name'] = fullNames.value[k]
            }
          }
        }
      }
      break;
    case 2:
      for (let i = 0; i < scheduleWithNicks.length; i++) {
        for (let j = 0; j < scheduleWithNicks[i]['teachers'].length; j++) {
          for (let k = 0; k < teachers.length; k++) {
            if (teachers[k] == scheduleWithNicks[i]['teachers'][j]['name']) {
              if (fullNames.value[k].split(' ').length == 3) {
                let splittedFIO = fullNames.value[k].split(' ')
                let newName = splittedFIO[1] + ' ' + splittedFIO[2] + ' ' + splittedFIO[0]
                scheduleWithNicks[i]['teachers'][j]['name'] = newName
              }
              else scheduleWithNicks[i]['teachers'][j]['name'] = fullNames.value[k]
            }
          }
        }
      }
      break;
  }
  emit('schedule', scheduleWithNicks)
}
</script>

<template>
    <pre>
        Ожидайте загрузки ФИО преподавателей, затем дополните ячейки куда не загрузилось полное ФИО (не обязательно)

        Сотрите ФИО преподавателя, если хотите убрать упоминание о нём в расписании
        (применяется для всех предметов, не советую злоупотреблять)
    </pre>
    <div v-for="value, key in teachers" class="grid">
      <div class="div-border name">{{ value }}</div>
      <textarea class="div-border nick" placeholder="—" v-model="fullNames[key]"></textarea>
    </div>
    <pre>
        Выберите формат ФИО преподавателей
    </pre>
    <button @click='setName(0)'>Фамилия И.О.</button>
    <button @click='setName(1)'>Фамилия Имя Отчество</button>
    <button @click='setName(2)'>Имя Отчество Фамилия</button>
</template>

<style scoped>
</style>