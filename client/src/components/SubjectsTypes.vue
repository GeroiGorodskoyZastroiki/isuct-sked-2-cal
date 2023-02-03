<script setup>
const props = defineProps(['schedule'])
const emit = defineEmits(['schedule'])

let scheduleWithTypes = props.schedule

let original = ['Лк.', 'Пр.з.', 'Лаб.']
let full = ['Лекция', 'Практика', 'Лаборатория']
let capitals = ['Л', 'П', 'ЛР']
let short = ['Лек', 'Пр', 'Лаб']

function changeTypes(event) {
  let pickedTypeVariant = event.target.textContent.split(' ')
  let dict = {}
  for (let i = 0; i < original.length; i++) {
    dict[original[i].toLowerCase()] = pickedTypeVariant[i]
  }
  for (let i = 0; i < scheduleWithTypes.length; i++) {
    scheduleWithTypes[i]['type'] = dict[scheduleWithTypes[i]['type']]
    if (scheduleWithTypes[i]['type'] == undefined) scheduleWithTypes.splice(i, 1)
  }
  emit('schedule', scheduleWithTypes)
}
</script>

<template>
    <pre>
        Можете выбрать обозначения для типов предметов
    </pre>
    <button @click='changeTypes($event)'>{{ full.toString().replace(/,/g, ' ') }}</button>
    <button @click='changeTypes($event)'>{{ original.toString().replace(/,/g, ' ') }}</button>
    <button @click='changeTypes($event)'>{{ capitals.toString().replace(/,/g, ' ') }}</button>
    <button @click='changeTypes($event)'>{{ short.toString().replace(/,/g, ' ') }}</button>
</template>

<style scoped>
</style>