# Triggering githubs actions manually
# This is my first Flask app
from flask import Flask, jsonify, Response, request, render_template # type: ignore
import pandas as pd
import matplotlib.pyplot as plt 
import io
import os

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    csv_path = os.path.join(os.path.dirname(__file__), '../smart_logistics_dataset.csv')
    try:
        df = pd.read_csv(csv_path)
        total_shipments = int(df.shape[0])
        delayed_shipments = int(df[df['Logistics_Delay'] > 0].shape[0]) if 'Logistics_Delay' in df.columns else 0
        average_delay = float(df['Logistics_Delay'].mean()) if 'Logistics_Delay' in df.columns else 0
    except Exception:
        total_shipments = delayed_shipments = average_delay = 0
    return render_template('dashboard.html', total_shipments=total_shipments, delayed_shipments=delayed_shipments, average_delay=average_delay)

# New route to display logistics data
@app.route('/logistics')
def show_logistics():
    csv_path = os.path.join(os.path.dirname(__file__), '../smart_logistics_dataset.csv')
    try:
        df = pd.read_csv(csv_path)
        # Showing first 20 rows for brevity
        data = df.head(20).to_dict(orient='records')
        return jsonify(data)
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/logistics/delay')
def analyze_logistics_delay():
    csv_path = os.path.join(os.path.dirname(__file__), '../smart_logistics_dataset.csv')
    try:
        df = pd.read_csv(csv_path)
        #trying to infer delay based on some logic
        if 'Logistics_Delay' in df.columns:
            average_delay = float(df['Logistics_Delay'].mean())
            max_delay = int(df['Logistics_Delay'].max())
            delayed_shipments = int(df[df['Logistics_Delay'] > 0].shape[0])
            total_shipments = int(df.shape[0])
        
        elif 'expected_delivery_time' in df.columns and 'actual_delivery_time' in df.columns:
            df['expected_delivery_time'] = pd.to_datetime(df['expected_delivery_time'])
            df['actual_delivery_time'] = pd.to_datetime(df['actual_delivery_time'])
            df['Logistics_Delay'] = (df['actual_delivery_time'] - df['expected_delivery_time']).dt.total_seconds() / 60
            average_delay = df['Logistics_Delay'].mean()
            max_delay = df['Logistics_Delay'].max()
            delayed_shipments = df[df['Logistics_Delay'] > 0].shape[0]
            total_shipments = df.shape[0]
            
        else:
            return jsonify(error="Delay data not available in the dataset"), 400
        
        return jsonify({
            "average_Logistics_Delay": average_delay,
            "max_delay": max_delay,
            "delayed_shipments": delayed_shipments,
            "total_shipments": total_shipments
        })
    except Exception as e:
        return jsonify(error=str(e)), 500
        
@app.route('/logistics/delay-plot')
def plot_logistics_delay():
    csv_path = os.path.join(os.path.dirname(__file__), '../smart_logistics_dataset.csv')
    try:
        df = pd.read_csv(csv_path)
        # Check if the Logistics_Delay column exists
        if 'Logistics_Delay' in df.columns:
            # Count delayed vs on-time
            delay_counts = df['Logistics_Delay'].value_counts().sort_index()
            labels = ['On Time', 'Delayed'] if 0 in delay_counts.index and 1 in delay_counts.index else delay_counts.index.astype(str)
            plt.figure(figsize=(6,4))
            delay_counts.plot(kind='bar', color=['green', 'red'], rot=0)
            plt.title('Logistics Delay Distribution')
            plt.xlabel('Status')
            plt.ylabel('Number of Shipments')
            plt.xticks(ticks=[0,1], labels=labels)
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return Response(buf.getvalue(), mimetype='image/png')
        else:
            return jsonify(error="Logistics_Delay column not found in the dataset"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500
    

    
@app.route('/logistics/delay/timeseries')
def plot_logistics_delay_timeseries():
    csv_path = os.path.join(os.path.dirname(__file__), '../smart_logistics_dataset.csv')
    try:
        df = pd.read_csv(csv_path)
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        if 'Logistics_Delay' in df.columns:
            df.set_index('Timestamp', inplace=True)
            daily_delays = df['Logistics_Delay'].resample('D').mean()
            plt.figure(figsize=(10, 5))
            daily_delays.plot(kind='line', title='Daily Delayed Shipments')
            plt.xlabel('Days')
            plt.ylabel('Total Delayed Shipments')
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return Response(buf.getvalue(), mimetype='image/png')
            
    except Exception as e:
        return jsonify(error=str(e)), 500

@app.route('/logistics/user_purchase_frequency')
def user_purchase_frequency():
    csv_path = os.path.join(os.path.dirname(__file__), '../smart_logistics_dataset.csv')
    try:
        df = pd.read_csv(csv_path)
        if 'User_Purchase_Frequency' in df.columns:
            plt.figure(figsize=(8,5))
            df['User_Purchase_Frequency'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
            plt.title('User Purchase Frequency Distribution')
            plt.xlabel('Purchase Frequency')
            plt.ylabel('Number of Users')
            plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return Response(buf.getvalue(), mimetype='image/png')
        else:
            return jsonify(error="User_Purchase_Frequency column not found in the dataset"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500
            


if __name__ == '__main__':
    app.run(debug=True)