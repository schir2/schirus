import moment from 'moment'

export function formatDate(value: string) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY')
  }
  return value
}