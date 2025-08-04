import sqlite3
import time
import os

DB_PATH = 'sales.db'  # SQLite DB file for demo

def setup_database():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Create table and insert data
    c.executescript(open('database_setup.sql').read())
    conn.commit()
    conn.close()

def run_query(query, conn):
    start_time = time.time()
    cursor = conn.execute(query)
    rows = cursor.fetchall()
    duration = time.time() - start_time
    return rows, duration

def main():
    if not os.path.exists(DB_PATH):
        setup_database()

    conn = sqlite3.connect(DB_PATH)
    
    original_query = '''
    SELECT product_id,
           SUM(quantity) AS total_quantity,
           SUM(quantity * price) AS total_revenue
    FROM sales
    GROUP BY product_id;
    '''
    
    # Run original query
    print("Running Original Query...")
    orig_result, orig_time = run_query(original_query, conn)
    
    # For SQLite, indexing benefits can be demonstrated by adding an index
    print("Creating index for Optimization...")
    conn.execute('CREATE INDEX IF NOT EXISTS idx_product_id ON sales(product_id);')
    
    # Run optimized query (same SQL but with index)
    print("Running Optimized Query...")
    opt_result, opt_time = run_query(original_query, conn)
    
    # Save output and performance comparisons
    with open('query_performance_report.txt', 'w') as f:
        f.write(f"Original Query Execution Time: {orig_time:.4f} seconds\n")
        f.write(f"Optimized Query Execution Time: {opt_time:.4f} seconds\n\n")
        f.write(f"Query Result:\n{opt_result}\n")
    
    print("Performance report saved to query_performance_report.txt")
    conn.close()

if __name__ == "__main__":
    main()
