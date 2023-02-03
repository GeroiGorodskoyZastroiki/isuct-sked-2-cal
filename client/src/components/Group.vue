<script setup>
import { ref } from 'vue'
import '../utils.js'

let inProgress = ref(false)
let groupNumber = ref('')
const emit = defineEmits(['schedule'])

function getGroup() {
    inProgress.value = true
    fetch('https://cors-anywhere.herokuapp.com/https://forms.isuct.ru/timetable/rvuzov')
    .then(result => result.json())
    .then((output) => {
        for (let i = 0; i < output['faculties'].length; i++) {
            for (let j = 0; j < output['faculties'][i]['groups'].length; j++) {
                if (output['faculties'][i]['groups'][j]['name'] == groupNumber.value.replaceAt(1, "-")) {
                    let schedule = output['faculties'][i]['groups'][j]['lessons']
                        for (let a = 0; a < schedule.length; a++) {
                            if (schedule[a]['type'] == '—') schedule.splice(a, 1)
                            for (let b = 0; b < schedule[a]['teachers'].length; b++) {
                                if (schedule[a]['teachers'][b]['name'] == '—') {
                                    if (schedule[a]['teachers'].length > 1) {
                                        schedule[a]['teachers'].splice(b, 1) 
                                    }
                                    else {
                                        schedule[a]['teachers'][b]['name'] = ''
                                    }
                                }
                            }
                        }
                    emit('schedule', schedule)
                }
            }
        }
    })
}
</script>

<template>
    <pre>
        Введите курс и номер своей группы
        (Например: 3/147)
    </pre>
    <input v-model="groupNumber" placeholder="—">
    <button v-if="inProgress === false" @click='getGroup'>Далее</button>
    <pre v-else-if="inProgress === true">
        Запрашиваем данные
        Ожидайте... (долго)
    </pre>
</template>

<style scoped>
</style>