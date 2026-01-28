import google.generativeai as genai
from django.shortcuts import render
from .models import JournalEntry

def index(request):
    # 1. Fetch history for the template
    history = JournalEntry.objects.all().order_by('-created_at')
    
    ai_advice = ""
    user_text = ""

    if request.method == "POST":
        user_text = request.POST.get("journal_entry")
        
        # 2. CONFIGURE KEY RIGHT BEFORE USE
        # Replace this string with your real key
        MY_API_KEY = "AIzaSyB1Q8CKe417Z8PO0KvtXbn4VUBjentxnDQ" 
        genai.configure(api_key=MY_API_KEY)
        
        try:
            # 3. Initialize model
            model = genai.GenerativeModel("gemini-2.5-flash")
            
            # 4. Generate and Save
            response = model.generate_content(user_text)
            ai_advice = response.text
            
            JournalEntry.objects.create(user_text=user_text, ai_advice=ai_advice)
            
            # Refresh history after saving new entry
            history = JournalEntry.objects.all().order_by('-created_at')
            
        except Exception as e:
            # This prints the error to your terminal for debugging
            print(f"DEBUG ERROR: {e}")
            ai_advice = f"Gemini's Insight: {e}"

    return render(request, 'index.html', {'advice': ai_advice, 'history': history})