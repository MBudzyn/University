import { calculate } from './calculator'

const display = document.getElementById('display') as HTMLDivElement
let current = ''

export function setupUI() {
  document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
      const key = button.getAttribute('data-key')
      if (!key) return

      if (key === 'C') {
        current = ''
      } else if (key === '←') {
        current = current.slice(0, -1)
      } else if (key === '=') {
        current = calculate(current)
      } else {
        current += key
      }

      display.textContent = current || '0'
    })
  })
}
