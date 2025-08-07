# Logistics Analytics Dashboard

A Flask-based web dashboard for visualizing and analyzing logistics data, shipment delays, and user purchase frequency.

## Features

- 📦 Visualizes total and delayed shipments
- 📊 Delay distribution and weekly delay trends
- 👤 User purchase frequency analysis
- 📅 Time series and histogram plots
- ⚡ Interactive dashboard with Bootstrap styling
- 🧑‍💻 Easy to extend with new filters and insights

## Demo

<img width="355" height="128" alt="image" src="https://github.com/user-attachments/assets/180d143a-2ef5-4648-8feb-366006dfc21b" />

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Place your `smart_logistics_dataset.csv` file in the project directory.

### Running the App

```bash
python app.py
```

Visit [http://localhost:5000/dashboard] in your browser.

## Project Structure

```
.
├── app.py
├── test_app.py
├── templates/
│   └── dashboard.html
├── smart_logistics_dataset.csv
└── requirements.txt
```

## Example Insights

- **Delay Distribution:** See the proportion of on-time vs delayed shipments.
- **Weekly Delayed Shipments:** Track trends in delays over time.
- **User Purchase Frequency:** Identify your most frequent buyers.

## Customization

- Add new plots or filters by editing `app.py` and `dashboard.html`.
- Style the dashboard using Bootstrap or custom CSS.

## License

MIT License

---

*Built with Flask, pandas, matplotlib, and Bootstrap.*
