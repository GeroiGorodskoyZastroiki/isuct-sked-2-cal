<script setup>
import { ref } from 'vue'
import Schema from './components/Schema.vue'
import Group from './components/Group.vue'
import SubjectsNicks from './components/SubjectsNicks.vue'
import SubjectsTypes from './components/SubjectsTypes.vue'
import TeachersNicks from './components/TeachersNicks.vue'
import TeachersPick from './components/TeachersPick.vue'
import Calendar from './components/Calendar.vue'

let schedule = ''
let step = ref('')
let stepQ = ['group', 'subjectsTypes', 'teachersNicks', 'subjectsNicks', 'schema', 'calendar']
step.value = stepQ.shift()

function updSchedule(modifiedSchedule) {
  schedule = modifiedSchedule
  console.log(schedule)
  step.value = stepQ.shift()
}
</script>

<template>
  <Group v-if="step === 'group'" @schedule="updSchedule" />
  <SubjectsTypes v-else-if="step === 'subjectsTypes'" @schedule="updSchedule" :schedule=schedule />
  <SubjectsNicks v-else-if="step === 'subjectsNicks'" @schedule="updSchedule" :schedule=schedule />
  <TeachersPick v-else-if="step === 'teachersPick'" @schedule="updSchedule" :schedule=schedule />
  <TeachersNicks v-else-if="step === 'teachersNicks'" @schedule="updSchedule" :schedule=schedule />
  <Schema v-if="step === 'schema'" @schedule="updSchedule" :schedule=schedule />
  <Calendar v-if="step === 'calendar'" :schedule=schedule />
</template>

<style scoped>
</style>