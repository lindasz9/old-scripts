function divbe_rendezes(array){
    gridDiv.innerHTML = ''
    array.forEach(i => {
        let div = document.createElement('div')
        div.textContent = i
        div.classList.add('cells')
        gridDiv.appendChild(div)
        if (i != null){
            div.style.backgroundColor = '#ffff99'
            div.addEventListener('click', () => {
                mozgatas(array, i, array.indexOf(i), div)
            })
        } 
    })
}

function mozgatas(array, number, index, div){
    if (index % 4 != 0 && array[index - 1] == null){
        array[index - 1] = number
    } else if (index % 4 != 3 && array[index + 1] == null){
        array[index + 1] = number
    } else if (index > 3 && array[index - 4] == null){
        array[index - 4] = number
    } else if (index < 12 && array[index + 4] == null){
        array[index + 4] = number
    } else{
        div.style.backgroundColor = '#f08080'
        div.classList.add('shake')
        setTimeout(() => {
            div.style.backgroundColor = '#ffff99'
            div.classList.remove('shake')
        }, 200)
        return
    }
    array[index] = null
    divbe_rendezes(array)

    if (start == true){
        count += 1
        turns.textContent = 'Lépések: ' + count

        if (check(array)){
            start = false
            turns.textContent = 'Lépések: ' + count
            divbe_rendezes(array)
            document.querySelectorAll('.cells').forEach(cell => {
                cell.style.backgroundColor = 'lightgreen'
            })

            setTimeout(() => {
                document.querySelectorAll('.cells').forEach(cell => {
                    if (cell.textContent == ''){
                        cell.style.backgroundColor = '#ffffff'
                    } else{
                        cell.style.backgroundColor = '#ffff99'
                    }
                });
            }, 1000);

            confetti({
                particleCount: 100,
            })

            setTimeout(() => {
                alert(`Gratulálok! Nyertél! ${count} lépés alatt kiraktad!`)
            }, 500)
        }
    }
}

function check(array){
    let correctCount = 0
    for (let i = 1; i < 16; i++){
        if (array[i - 1] == i){
            correctCount += 1
        }
    }
    return correctCount == 15
}

let gridDiv = document.querySelector('#grid_div')
let turns = document.querySelector('#turns')
let count = 0
let start = false

let sorrend = []
for (let i = 1; i < 17; i++){
    if (i == 16){
        sorrend.push(null)
    } else{
        sorrend.push(i)
    }
} 

divbe_rendezes(sorrend)

document.querySelector('#keveres').addEventListener('click', () => {
    count = 0
    start = true
    turns.textContent = 'Lépések: ' + count
    for (let i = 0; i < 10; i++){
        index = sorrend.indexOf(null)
        let random = Math.floor(Math.random() * 4) 
        if (index % 4 != 0 && random == 0){
            sorrend[index] = sorrend[index - 1]
            sorrend[index - 1] = null
        } else if (index % 4 != 3 && random == 1){
            sorrend[index] = sorrend[index + 1]
            sorrend[index + 1] = null
        } else if (index > 3 && random == 2){
            sorrend[index] = sorrend[index - 4]
            sorrend[index - 4] = null
        } else if (index < 12 && random == 3){
            sorrend[index] = sorrend[index + 4]
            sorrend[index + 4] = null
        } 
        divbe_rendezes(sorrend)
    }
})