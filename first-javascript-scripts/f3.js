function muveletGeneralas(parokSzama){
    let muveletek = []
    let eredmenyek = []
    while(muveletek.length != parokSzama){
        let random = Math.floor(Math.random() * 4)
        let muvelet
        let eredmeny
        if (random == 0 || random == 1){
            let szam1 = Math.ceil(Math.random() * 20)
            let szam2 = Math.ceil(Math.random() * 20)
            if (random == 0){
                muvelet = `${szam1} + ${szam2}`
                eredmeny = szam1 + szam2
            } else{
                if (szam2 > szam1){
                    let tmp = szam1
                    szam1 = szam2
                    szam2 = tmp
                }
                muvelet = `${szam1} - ${szam2}`
                eredmeny = szam1 - szam2
            }
        } else{
            let szam1 = Math.ceil(Math.random() * 10)
            let szam2 = Math.ceil(Math.random() * 10)
            if (random == 3){
                muvelet = `${szam1} * ${szam2}`
                eredmeny = szam1 * szam2
            } else{
                muvelet = `${szam1 * szam2} / ${szam1}`
                eredmeny = szam2
            }
        }
        if (!eredmenyek.includes(eredmeny)){
            muveletek.push(muvelet)
            eredmenyek.push(eredmeny)
        }
    }
    let kartyak = keveres([...muveletek, ...eredmenyek])
    divbeRendezes(kartyak)
}

function keveres(kartyak){
    let j
    let k
    for (let i = 0; i < 100; i++){
        j = Math.floor(Math.random() * kartyak.length)
        k = Math.floor(Math.random() * kartyak.length)
        let tmp = kartyak[j]
        kartyak[j] = kartyak[k]
        kartyak[k] = tmp
    }
    return kartyak
}

function divbeRendezes(kartyak){
    cardsDiv.innerHTML = ''
    kartyak.forEach((i, index) => {
        let div = document.createElement('div')
        div.textContent = ''
        div.classList.add('kartya')
        cardsDiv.appendChild(div)

        let fuggveny = felforditasElott(div, index, kartyak)
        div.fuggveny = fuggveny
        div.addEventListener('click', fuggveny)
    })
}

function felforditasElott(div, index, kartyak){
    return function(){
        felforditas(div, index, kartyak)
    }
}

function felforditas(div, index, kartyak){
    if (div.textContent != '') return

    if (felforditottakSzama == 2){
        if (visszaszamlalo){
            clearTimeout(visszaszamlalo)
            visszaszamlalo = 0
        }

        document.querySelectorAll('.kartya').forEach(i => {
            if (i.textContent != ''){
                visszaforditas(i)
            }
        })

        felforditottakSzama = 0
        felforditottak = []
    }

    div.classList.add('scale')
    setTimeout(() => div.classList.remove('scale'), 200)

    felforditottakSzama += 1
    felforditottak.push(kartyak[index])

    div.textContent = kartyak[index]
    div.style.backgroundColor = 'white'
    
    if (felforditottakSzama == 1){
        elsoDiv = div
    } else if (felforditottakSzama == 2){
        check([elsoDiv, div])
    }
}

function check(divek){
    felforditottak.forEach((i, index) => {
        if (typeof i == "string"){
            felforditottak[index] = eval(i)
        }
    })
    if (felforditottak[0] == felforditottak[1]){
        felforditottakSzama = 0
        felforditottak = []
        szamlalo += 1
        document.querySelector('#szamlalo').textContent = 'Megtalált párok: ' + szamlalo
        divek.forEach(i => {
            i.style.backgroundColor = 'lightgreen'
        })
        if (szamlalo == parokSzama){
            win()
        }
        setTimeout(() => {

            divek.forEach(i => {
                i.style.visibility = 'hidden'
                i.removeEventListener('click', i.fuggveny)
            })
        }, 1000)
    } else{
        visszaszamlalo = setTimeout(() => {
            divek.forEach(i => {
                visszaforditas(i)
            })
            felforditottakSzama = 0
            felforditottak = []
            visszaszamlalo = 0
        }, 3000)
    }
}

function visszaforditas(kartya){
    kartya.classList.add('scale')
    setTimeout(() => kartya.classList.remove('scale'), 200)
    kartya.textContent = ''
    kartya.style.backgroundColor = 'rgb(255, 212, 159)'
}

function win(){
    document.body.classList.add('flash')
    setTimeout(() => {
        document.body.classList.remove('flash')
    }, 400)

    setTimeout(() => {
        alert('Gratulálok! Megtaláltad az összes párt!')
        szamlalo = 0
        document.querySelector('#szamlalo').textContent = 'Megtalált párok: ' + szamlalo
        muveletGeneralas(parokSzama)  
    }, 500)
}

let cardsDiv = document.querySelector('#cards_div')
let parokSzama
let felforditottakSzama = 0
let felforditottak = []
let elsoDiv 
let visszaszamlalo = 0
let szamlalo = 0

muveletGeneralas(9)

document.querySelector('#generalas').addEventListener('click', () => {
    parokSzama = parseInt(document.querySelector('#parok_szama').value)
    document.querySelector('#parok_szama').value = ''

    felforditottakSzama = 0
    felforditottak = []
    szamlalo = 0
    visszaszamlalo = 0

    if (!Number.isInteger(parokSzama)){
        alert('Adj meg egy érvényes számot!')
    } else if(parokSzama > 15){
        alert('Maximum 15 legyen a párok száma')
    } else if(parokSzama < 1){
        alert('Ez most komoly?')
    } else{
        muveletGeneralas(parokSzama)
    } 
})

