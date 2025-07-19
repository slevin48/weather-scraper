# weather-scraper

GitHub Action to scrape the weather 🌥️⛅🌦️

![workflow](img/workflow.png)

## Schedule

```
┌───────────── minute (*/10 → every 10 minutes)
│ ┌─────────── hour   (*   → every hour)
│ │ ┌───────── day     (*   → every day of month)
│ │ │ ┌─────── month   (*   → every month)
│ │ │ │ ┌───── weekday (*   → every day of week)
│ │ │ │ │
*/10 * * * *
```