import os
from supabase import create_client, Client

SUPABASE_URL = "https://etxspcgqupwvngdvyogh.supabase.co"
SUPABASE_KEY = "sb_publishable_fprGNaIeLnl3Z8xk_T0bAw_Dwc61_nT"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
