import pandas as pd

# Load the CSV file from the user
try:
    df = pd.read_csv('Row read - Copy.csv')
    print("File 'Row read - Copy.csv' loaded successfully.")

    # --- Data Preparation ---

    # Split the original dataframe into two, based on the file's structure.
    # The first part contains the 'C' samples.
    df1 = df.iloc[:, :48].copy() # Use .copy() to avoid warnings

    # The second part contains the 'N' samples. We also rename its columns for consistency.
    df2 = df.iloc[:, 49:61].rename(columns={'gene_id.1': 'gene_id', 'gene_name': 'GeneSymbol'}).copy()

    # --- Data Cleaning ---

    # Clean the identifying columns in the first dataframe (df1)
    df1['GeneSymbol'] = df1['GeneSymbol'].str.strip()
    df1['gene_id'] = df1['gene_id'].str.strip()
    # Create a new column with the gene ID *without* the version number for matching
    df1['gene_id_no_version'] = df1['gene_id'].str.split('.').str[0]

    # Clean the identifying columns in the second dataframe (df2)
    df2['GeneSymbol'] = df2['GeneSymbol'].str.strip()
    df2['gene_id'] = df2['gene_id'].str.strip()
    # Create a new column with the gene ID *without* the version number for matching
    df2['gene_id_no_version'] = df2['gene_id'].str.split('.').str[0]
    
    # --- Merging and Finalizing ---

    # Perform an 'inner' merge. This finds rows where the 'GeneSymbol' and the
    # version-less 'gene_id' are present in BOTH dataframes.
    merged_df = pd.merge(df1, df2, on=['GeneSymbol', 'gene_id_no_version'], how='inner')

    if not merged_df.empty:
        print("\nSuccessfully found common genes!")
        
        # Clean up the final dataframe for a clean output.
        # We drop the extra columns created for the merge and rename the original gene_id column.
        final_df = merged_df.drop(columns=['gene_id_y', 'gene_id_no_version']).rename(columns={'gene_id_x': 'gene_id'})
        
        # Reorder the columns for better readability.
        c_cols = [col for col in final_df.columns if col.startswith('C')]
        n_cols = [col for col in final_df.columns if col.startswith('N')]
        id_cols = ['GeneSymbol', 'gene_id']
        
        final_df = final_df[id_cols + c_cols + n_cols]

        # Save the final, cleaned dataframe to a new CSV file.
        final_df.to_csv('common_genes_with_values.csv', index=False)
        print("The final data has been saved to 'common_genes_with_values.csv'")
        
        # Display the first few rows of the final result.
        print("\nPreview of the final data:")
        print(final_df.head())
    else:
        print("\nNo common genes were found after processing the file.")

except FileNotFoundError:
    print("Error: 'Row read - Copy.csv' not found. Please ensure it's in the correct directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")