import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def create_ocr_literature_timeline():
    """Create OCR Literature Timeline for presentation"""
    fig, ax = plt.subplots(figsize=(16, 10))
    
    # Timeline data
    years = [2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2021, 2022, 2024]
    technologies = [
        'Tesseract OCR\n(Ray Smith, HP)',
        'Statistical Pattern\nRecognition',
        'SVM for OCR\n(Cortes & Vapnik)',
        'Deep Learning\nRevolution (Hinton)',
        'CNN Architecture\n(LeCun et al.)',
        'Google Cloud\nVision API',
        'Attention\nMechanisms\n(Vaswani et al.)',
        'Vision Transformers\n(Dosovitskiy et al.)',
        'EasyOCR\n(CNN-based)',
        'Multi-modal\nAI Models',
        '⭐ VisionText Agent\n(Our Work) ⭐'
    ]
    
    # Color coding by era
    colors = [
        '#E74C3C',  # Traditional - Red
        '#E74C3C',  # Traditional - Red
        '#F39C12',  # ML Era - Orange
        '#2ECC71',  # Deep Learning - Green
        '#2ECC71',  # Deep Learning - Green
        '#3498DB',  # Deep Learning - Blue
        '#9B59B6',  # Attention Era - Purple
        '#1ABC9C',  # Transformer Era - Teal
        '#1ABC9C',  # Transformer Era - Teal
        '#34495E',  # Multi-modal - Dark
        '#FF1493'   # Our Work - Hot Pink
    ]
    
    # Create timeline bars
    bar_height = 0.7
    for i, (year, tech, color) in enumerate(zip(years, technologies, colors)):
        # Create horizontal bars
        bar = ax.barh(i, 2, left=year-1, height=bar_height, 
                     color=color, alpha=0.8, edgecolor='white', linewidth=2)
        
        # Add technology labels inside bars
        ax.text(year, i, tech, ha='center', va='center', 
               fontsize=11, fontweight='bold', color='white')
        
        # Add year labels
        ax.text(year-2.5, i, str(year), ha='center', va='center', 
               fontsize=12, fontweight='bold', color='black')
    
    # Customize the chart
    ax.set_yticks(range(len(years)))
    ax.set_yticklabels([])
    ax.set_xlabel('Year', fontsize=16, fontweight='bold')
    ax.set_title('Literature Insights: Evolution of OCR and Handwriting Recognition Methods', 
                fontsize=20, fontweight='bold', pad=30)
    ax.set_xlim(2004, 2026)
    ax.set_ylim(-0.5, len(years)-0.5)
    
    # Remove y-axis
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(left=False)
    
    # Add grid
    ax.grid(True, axis='x', alpha=0.3, linestyle='--')
    
    # Add legend
    traditional_patch = mpatches.Patch(color='#E74C3C', label='Traditional Methods (2006-2010)')
    ml_patch = mpatches.Patch(color='#F39C12', label='Machine Learning Era (2010-2012)')
    dl_patch = mpatches.Patch(color='#2ECC71', label='Deep Learning Revolution (2012-2018)')
    transformer_patch = mpatches.Patch(color='#1ABC9C', label='Transformer Era (2020-2022)')
    our_work_patch = mpatches.Patch(color='#FF1493', label='Our Contribution (2024)')
    
    ax.legend(handles=[traditional_patch, ml_patch, dl_patch, transformer_patch, our_work_patch], 
              loc='upper left', bbox_to_anchor=(0.02, 0.98), fontsize=12)
    
    # Add research insights text
    insights_text = """Key Research Findings: Evolution from template matching → statistical methods → deep learning → 
attention mechanisms → multi-stage agent architecture. Each advancement improved accuracy by 10-15%."""
    
    fig.text(0.5, 0.02, insights_text, ha='center', va='bottom', 
             fontsize=13, style='italic', wrap=True)
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1)
    plt.savefig('ocr_literature_timeline.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()
    print("✅ Created ocr_literature_timeline.png")

def main():
    """Generate OCR literature timeline for presentation"""
    print("🎨 Generating OCR Literature Timeline...")
    print("=" * 50)
    
    try:
        create_ocr_literature_timeline()
        
        print("=" * 50)
        print("🎉 Timeline generated successfully!")
        print("\nGenerated file:")
        print("📊 ocr_literature_timeline.png - Literature insights timeline")
        print("\n✅ Ready to add to your presentation!")
        
    except Exception as e:
        print(f"❌ Error generating timeline: {str(e)}")
        print("Please ensure matplotlib is installed:")
        print("pip install matplotlib numpy")

if __name__ == "__main__":
    main()