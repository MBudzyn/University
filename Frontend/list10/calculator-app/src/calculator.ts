import { evaluate } from 'mathjs'

export function calculate(expression: string): string {
  try {
    const result = evaluate(expression)
    return result.toString()
  } catch {
    return 'Error'
  }
}
