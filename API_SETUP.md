# Quick API Setup - Use Your Free $5 Credits

## Step 1: Install SDK
```bash
pip install anthropic
```

## Step 2: Get Free API Key
1. Go to: https://console.anthropic.com/
2. Sign up (you get $5 FREE credits)
3. Go to "API Keys"
4. Create new key
5. Copy it

## Step 3: Set API Key

**PowerShell:**
```powershell
$env:ANTHROPIC_API_KEY = "your-api-key-here"
```

**Or set permanently in Windows:**
- Search "Environment Variables"
- Add: `ANTHROPIC_API_KEY` = your-key

## Step 4: Run Script
```bash
cd C:\AllScripts\Personal\SMV
python api_rephrase.py
```

## What It Does:
- ✓ Checks what's already done (100 slokas)
- ✓ Processes remaining ~908 slokas
- ✓ Saves progress every 10 slokas
- ✓ Can resume if interrupted
- ✓ Takes ~30 minutes
- ✓ Costs ~$2.70 (you have $5 free!)

## After It Completes:
Let me know and I'll verify all 1,008 slokas are complete and help with any final cleanup!
