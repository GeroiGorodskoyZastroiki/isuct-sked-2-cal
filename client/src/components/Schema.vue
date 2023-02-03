<script setup>
import { ref } from 'vue'
const props = defineProps(['schedule'])
const emit = defineEmits(['schedule'])

let schema = ref('')
let defaultSchemas = ['Т Н А П', 'Н А П', 'Т Н А', 'Н А']
let scheduleWithSchema = props.schedule

function setSchema(number) {
    schema.value = defaultSchemas[number]  
    combineParameters()
}

function combineParameters() {
    let aboba = schema.value.split(' ')
    for (let i = 0; i < scheduleWithSchema.length; i++) {
        scheduleWithSchema[i]['name'] = ''
        for (let j = 0; j < aboba.length; j++) {
            switch (aboba[j]) {
                case 'Т':
                    scheduleWithSchema[i]['name'] += scheduleWithSchema[i]['type']
                    break;
                case 'Н':
                    scheduleWithSchema[i]['name'] += scheduleWithSchema[i]['subject']
                    break;
                case 'А':
                    let auditorii = ''
                    for (let k = 0; k < scheduleWithSchema[i]['audiences'].length; k++) {
                        if (auditorii != '') {
                            auditorii += '\/'
                            auditorii += scheduleWithSchema[i]['audiences'][k]['name']
                        }
                        else auditorii += scheduleWithSchema[i]['audiences'][k]['name']
                    }
                    scheduleWithSchema[i]['name'] += auditorii
                    break;
                case 'П':
                    let prepodi = ''
                    for (let k = 0; k < scheduleWithSchema[i]['teachers'].length; k++) {
                        if (scheduleWithSchema[i]['teachers'][k]['name'] != '') {
                            if (prepodi != '') {
                                prepodi += '\/'
                                prepodi += scheduleWithSchema[i]['teachers'][k]['name']
                            }
                            else prepodi += scheduleWithSchema[i]['teachers'][k]['name']
                        }
                    }
                    scheduleWithSchema[i]['name'] += prepodi
                    break;
            }
            scheduleWithSchema[i]['name'] += ' '
        }
    }
    emit('schedule', scheduleWithSchema)
}
</script>

<template>
    <pre>
        Выберите схему компоновки названия пары

        Т - Тип пары
        Н - Название предмета
        А - Аудитория
        П - ФИО преподавателя
    </pre>
    <button @click='setSchema(0)'>{{ defaultSchemas[0] }}</button>
    <button @click='setSchema(1)'>{{ defaultSchemas[1] }}</button>
    <button @click='setSchema(2)'>{{ defaultSchemas[2] }}</button>
    <button @click='setSchema(3)'>{{ defaultSchemas[3] }}</button>
    <pre>
        или составьте свою
        (введите обозначения параметров заглавными буквами через пробел)
    </pre>
    <input v-model="schema" placeholder="—">
    <button @click='combineParameters'>Использовать свою</button>
</template>

<style scoped>
</style>