#!/usr/bin/env python3
"""
Validate ChIP-seq pipeline configuration
Checks for required settings and potential issues
"""

import os
import yaml

def validate_pipeline_config():
    """Validate the snakemake pipeline configuration"""
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(script_dir, "snakemake_ChIPseq_pipeline", "config.yaml")
    srr_list_file = os.path.join(script_dir, "pipeline", "SRR_Acc_List.txt")
    snakefile = os.path.join(script_dir, "snakemake_ChIPseq_pipeline", "Snakefile")
    
    print()
    print("=" * 80)
    print("ChIP-seq PIPELINE CONFIGURATION VALIDATION")
    print("=" * 80)
    print()
    
    # Check files exist
    print("FILE EXISTENCE CHECK")
    print("-" * 80)
    
    files_to_check = {
        "Configuration file (config.yaml)": config_file,
        "SRR accession list": srr_list_file,
        "Snakefile": snakefile,
    }
    
    all_exist = True
    for name, filepath in files_to_check.items():
        exists = os.path.exists(filepath)
        status = "✓" if exists else "✗"
        print(f"  {status} {name}: {filepath}")
        all_exist = all_exist and exists
    print()
    
    if not all_exist:
        print("ERROR: Some required files are missing!")
        return False
    
    # Load and validate configuration
    print("CONFIGURATION CONTENT")
    print("-" * 80)
    
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        if config is None:
            config = {}
        
        print(f"Configuration loaded successfully:")
        print()
        for key, value in config.items():
            print(f"  {key}: {value}")
        print()
    except Exception as e:
        print(f"ERROR: Failed to load config.yaml: {e}")
        return False
    
    # Validate required parameters
    print("CONFIGURATION VALIDATION")
    print("-" * 80)
    
    required_keys = ["idx_bt1", "macs_g"]
    all_valid = True
    
    for key in required_keys:
        if key in config:
            print(f"  ✓ {key}: {config[key]}")
        else:
            print(f"  ✗ Missing required parameter: {key}")
            all_valid = False
    print()
    
    # Check SRR list
    print("SRR ACCESSION LIST VALIDATION")
    print("-" * 80)
    
    try:
        with open(srr_list_file, 'r') as f:
            srr_ids = [line.strip() for line in f if line.strip()]
        
        print(f"  ✓ SRR list loaded successfully")
        print(f"  ✓ Total samples: {len(srr_ids)}")
        print(f"  ✓ Sample range: {srr_ids[0]} to {srr_ids[-1]}")
        print()
    except Exception as e:
        print(f"  ✗ Failed to load SRR list: {e}")
        return False
    
    # Check directories
    print("REQUIRED DIRECTORIES CHECK")
    print("-" * 80)
    
    pipeline_dir = os.path.join(script_dir, "snakemake_ChIPseq_pipeline")
    required_dirs = {
        "rawfastqs/": os.path.join(pipeline_dir, "rawfastqs"),
        "envs/": os.path.join(pipeline_dir, "envs"),
        "output directories": [
            os.path.join(pipeline_dir, "01seq"),
            os.path.join(pipeline_dir, "02fqc"),
            os.path.join(pipeline_dir, "03seqClean"),
            os.path.join(pipeline_dir, "04aln"),
            os.path.join(pipeline_dir, "05peak"),
        ]
    }
    
    # Check rawfastqs and envs
    for dir_name, dir_path in list(required_dirs.items())[:2]:
        exists = os.path.exists(dir_path)
        status = "✓" if exists else "⚠"
        print(f"  {status} {dir_name}: {dir_path}")
    
    print()
    print("  Output directories (will be created during pipeline run):")
    for dir_path in required_dirs["output directories"]:
        exists = os.path.exists(dir_path)
        status = "✓" if exists else "○"
        print(f"    {status} {os.path.basename(dir_path)}/")
    print()
    
    # Check conda environments
    print("CONDA ENVIRONMENTS CHECK")
    print("-" * 80)
    
    envs_dir = os.path.join(pipeline_dir, "envs")
    if os.path.exists(envs_dir):
        env_files = [f for f in os.listdir(envs_dir) if f.endswith('.yaml')]
        print(f"  ✓ Found {len(env_files)} environment definitions:")
        for env_file in sorted(env_files):
            print(f"    - {env_file}")
    else:
        print(f"  ✗ envs/ directory not found")
    print()
    
    # Summary
    print("VALIDATION SUMMARY")
    print("-" * 80)
    
    if all_valid:
        print("✓ Configuration appears valid!")
        print()
        print("Ready to run analysis with commands:")
        print()
        print("  cd snakemake_ChIPseq_pipeline")
        print("  conda activate chipseq")
        print("  snakemake -n  # Dry run first")
        print("  snakemake --cores all --use-conda")
        print()
    else:
        print("⚠ Configuration needs review/fixes before running pipeline")
        print()
    
    print("=" * 80)
    print()
    
    return all_valid

if __name__ == "__main__":
    try:
        validate_pipeline_config()
    except Exception as e:
        print(f"Error during validation: {e}")
