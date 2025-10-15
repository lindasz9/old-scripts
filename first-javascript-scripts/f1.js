function errorCatching(szam, hibaHely, gomb){
    gomb.style.backgroundColor = 'red'
    if (isNaN(szam)){
        //alert('Számnak kell lennie!')
        hibaHely.textContent = 'Számnak kell lennie!'
        return true
    } else if (szam > names.length){
        hibaHely.textContent = 'Túl nagy szám!'
        return true
    } else if(szam < 0){
        hibaHely.textContent = 'Nem lehet negatív a szám'
        return true
    }
    gomb.style.backgroundColor = ''
    hibaHely.textContent = ''
    return false
}

function randomOrder(order, array, int){
    for (let i = 0; i < int; i++){
        let random = array[Math.floor(Math.random() * array.length)]
        order.push(random)
        let index = array.indexOf(random)
        array.splice(index, 1)
    }
}

document.querySelectorAll('button').forEach(i => {
    i.addEventListener('click', () => {
        i.classList.add('shake')
        setTimeout(() => {
            i.classList.remove('shake')
        }, 500)
    })
})

let namesInput = document.querySelector('#names')
let names
namesInput.addEventListener('input', function(){
    let namesString = namesInput.value
    let namesArray = namesString.split(/[\s,]+/)
    names = namesArray.map(i => i.trim())
});

document.querySelector('#names_delete').addEventListener('click', function(){
    namesInput.value = ''
    names = []
})

//A
document.querySelector('#sorsolas').addEventListener('click', function(){
    
    let people = parseInt(document.querySelector('#people').value)
    let sorsoltNevek = document.querySelector('#sorsolt_nevek')
    sorsoltNevek.innerHTML = ''

    let AHiba = document.querySelector('#A_hiba')
    if (errorCatching(people, AHiba, document.querySelector('#sorsolas'))){
        return
    } 

    let namesCopy = [...names]
    let randomNames = [] 
    randomOrder(randomNames, namesCopy, people)

    randomNames.forEach(i => {
        let li = document.createElement('li')
        li.textContent = i
        li.classList.add('slide')
        sorsoltNevek.appendChild(li)
    })
})

//B
document.querySelector('#sorrend').addEventListener('click', function(){
    let namesCopy = [...names]
    let orderedNames = []
    randomOrder(orderedNames, namesCopy, names.length)
    
    let sorbanNevek = document.querySelector('#sorban_nevek')
    sorbanNevek.innerHTML = ''
    orderedNames.forEach((value, index) => {
        setTimeout(() => {
            let li = document.createElement('li')
            li.textContent = value
            li.classList.add('scale')
            sorbanNevek.appendChild(li)
        }, index * 100)
    })
})

//C
document.querySelector('#rendezes').addEventListener('click', function(){
    let fo = parseInt(document.querySelector('#fo').value)
    let table = document.querySelector('#csoport_table')
    table.innerHTML = ''

    let CHiba = document.querySelector('#C_hiba')
    if (errorCatching(fo, CHiba, document.querySelector('#rendezes'))){
        return
    }

    let namesCopy = [...names]
    let randomNames = []
    randomOrder(randomNames, namesCopy, names.length)

    //a csoportokban a fők száma különbsége max 1
    let foDarab = 0
    let foMinusDarab = 0
    while (true){
        if (names.length % fo < fo - 1 && names.length % fo != 0){
            remain = fo - names.length % fo
            if (Math.ceil(names.length / fo) >= remain){
                foDarab = Math.ceil(names.length / fo) - remain
                foMinusDarab = Math.ceil(names.length / fo) - foDarab
                break
            } else{
                fo--
            }
        } else{
            if (names.length % fo == 0){
                foDarab = Math.ceil(names.length / fo) - names.length % fo
            } else{
                foDarab = Math.ceil(names.length / fo) - fo + names.length % fo
            }
            foMinusDarab = Math.ceil(names.length / fo) - foDarab
            break
        }
    }

    //a csoportok fői darabszáma sorban
    let fo_szam = []
    for (let i = 0; i < foDarab; i++){
        fo_szam.push(fo)
    }
    for (let i = 0; i < foMinusDarab; i++){
        fo_szam.push(fo - 1)
    }

    //kétdimenziós listába rendezése a neveknek csoportok szerint
    let lists = []
    let index = 0
    for (let hossz of fo_szam){
        let list = randomNames.slice(index, index + hossz)
        lists.push(list)
        index += hossz
    }

    //táblázatba rendezés
    function generateTable(){
        let row
        let cell
        let ol
        let count = 0
        lists.forEach((value, index) => {
            setTimeout(() => {
                if (count % 4 == 0){
                    row = table.insertRow()
                }
                cell = row.insertCell()
                ol = document.createElement('ol')
                ol.classList.add('scale')
                cell.appendChild(ol)
                value.forEach(j => {
                    let li = document.createElement('li')
                    li.textContent = j
                    ol.appendChild(li)
                })
                count++
            }, index * 300)
        })
    }
    
    //töltés...
    let loading = document.querySelector('#loading')
    for (let i = 0; i < 4; i++){
        setTimeout(() => {
            if (i == 3){
                loading.textContent = ''
                generateTable()
            } else {
                loading.textContent = 'töltés.' + '.'.repeat(i)
            }
        }, i * 1000)
    }
})