#!/usr/bin/env python3
"""
Kenworks Ventures — static product-page generator.

This is an OPTIONAL authoring tool. The website itself stays 100% static HTML
(no build step needed to serve on GitHub Pages). Run this only when you want to
regenerate the /products/ pages, division indexes, sitemap.xml and robots.txt
after editing the product data below:

    python3 tools/generate.py

Edit specs/copy here, then re-run. Hand edits to generated /products/*.html will
be overwritten on the next run — change the data in this file instead.
"""
import os, html

BASE = "https://dgm688.github.io/kenworks-ventures"
WA = "254722706416"
EMAIL = "info@kenworksventures.co.ke"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTS_DIR = os.path.join(ROOT, "products")

DIVISIONS = {
    "insulation": {
        "slug": "thermal-acoustic-insulation",
        "name": "Thermal & Acoustic Insulation",
        "h1": "Thermal & Acoustic Insulation Materials in Nairobi, Kenya",
        "title": "Thermal & Acoustic Insulation in Kenya | Supplier & Price — Kenworks Ventures",
        "meta": "Supplier of thermal and acoustic insulation in Nairobi, Kenya — rockwool, ceramic fiber, fiberglass, armaflex, calcium silicate and more. Direct importer, same-day WhatsApp quotes.",
        "intro": "Kenworks Ventures is a direct importer and supplier of thermal and acoustic insulation materials in Nairobi, Kenya. From high-temperature ceramic fiber and rockwool to fiberglass, armaflex and roof insulation, we hold deep stock and give spec-matched advice for industrial plant, buildings and HVAC. We supply across Kenya and export to Uganda, Tanzania and Rwanda.",
    },
    "refractory": {
        "slug": "refractory-materials",
        "name": "Refractory Materials",
        "h1": "Refractory Materials & Firebricks in Nairobi, Kenya",
        "title": "Refractory Materials & Firebricks in Kenya | Supplier & Price — Kenworks Ventures",
        "meta": "Supplier of refractory materials in Nairobi, Kenya — 40% & 70% alumina firebricks, zirconia bricks, Maxheat castable cements, mortar, ceramic ropes and gaskets rated up to 2000°C. Direct importer.",
        "intro": "Kenworks Ventures is one of Kenya's main distributors of refractory materials, supplying firebricks, castable cements, mortars and high-temperature sealing products rated up to 2000°C. We stock 40% and 70% alumina firebricks, zirconia bricks, Maxheat castables and ceramic fiber sealing for furnaces, kilns, boilers and incinerators — with delivery across Kenya and East Africa.",
    },
    "electrical": {
        "slug": "electrical-power",
        "name": "Electrical Safety & Power",
        "h1": "Electrical Safety Mats & Generator Servicing in Nairobi, Kenya",
        "title": "H.V Electrical Insulating Mats & Generator Servicing in Kenya — Kenworks Ventures",
        "meta": "High-voltage electrical insulating rubber mats (Class 0–4, 10–50kV, ASTM D178) and generator servicing in Nairobi, Kenya. Keeping you powered up at all times — Kenworks Ventures.",
        "intro": "Kenworks Ventures supplies electrical safety equipment and power-support services in Nairobi, Kenya. Our high-voltage insulating rubber mats protect personnel in substations and control rooms, and our generator servicing keeps petrol and diesel sets running. True to our promise — keeping you powered up at all times.",
    },
}

# Each product: slug, name, div, temp(badge), img, h1, title, meta,
# specs [(label,value)], apps [..], copy [para, para]
PRODUCTS = [
 dict(slug="ceramic-fiber-blanket", name="Ceramic Fiber Blanket", div="insulation", temp="1260°C", img="ceramic-fiber-blanket",
  h1="Ceramic Fiber Blanket in Nairobi, Kenya",
  title="Ceramic Fiber Blanket in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy ceramic fiber blanket in Nairobi, Kenya. 1260°C, 128 kg/m³, 7620×610×25/50mm. Direct importer & supplier — same-day WhatsApp quotes from Kenworks Ventures.",
  specs=[("Max service temperature","1260°C"),("Material","High-purity alumina-silica ceramic fiber"),("Density","128 kg/m³"),("Dimensions","7620mm × 610mm × 25mm and 3600mm × 610mm × 50mm"),("Thickness options","25mm, 50mm"),("Price","{{PRICE_PER_ROLL}} — request a quote")],
  apps=["Furnace and kiln hot-face lining","Boiler and oven insulation","Fire protection and back-up lining","Expansion joints and high-temperature wrapping"],
  copy=["Ceramic fiber blanket is a lightweight, flexible insulation made from spun high-purity alumina-silica fibers. It withstands continuous service at 1260°C while staying easy to cut, wrap and fit, which makes it the default choice for lining furnaces, kilns, boilers and ovens. Its low thermal mass means faster heat-up and lower fuel costs compared with dense refractory linings.",
        "Kenworks Ventures stocks ceramic fiber blanket at 128 kg/m³ density in both 25mm and 50mm thicknesses, supplied in full rolls. We import directly, so pricing stays competitive and stock stays deep for industrial clients across Nairobi and the wider East African market. Tell us your operating temperature and surface area and we will recommend the right thickness and density for the job."]),
 dict(slug="ceramic-fiber-board", name="Ceramic Fiber Board", div="insulation", temp="1260°C", img="ceramic-fiber-board",
  h1="Ceramic Fiber Board in Nairobi, Kenya",
  title="Ceramic Fiber Board in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy ceramic fiber board in Nairobi, Kenya. Rigid 1260°C board, 320 kg/m³, 600×300×50mm. Direct importer & supplier — same-day WhatsApp quotes from Kenworks Ventures.",
  specs=[("Max service temperature","1260°C"),("Material","Rigid alumina-silica ceramic fiber"),("Density","320 kg/m³"),("Dimensions","600mm × 300mm × 50mm"),("Form","Rigid, self-supporting board"),("Price","{{PRICE_PER_BOARD}} — request a quote")],
  apps=["Furnace and kiln rigid lining","Fire protection panels","Back-up insulation behind firebrick","Hot-face board where mechanical strength is needed"],
  copy=["Ceramic fiber board is a rigid, self-supporting panel made from alumina-silica fibers. Unlike blanket, it holds its shape under light load, giving you a clean structural hot-face for furnace linings, fire-protection panels and back-up insulation. It offers excellent thermal resistance and low conductivity at temperatures up to 1260°C while remaining far lighter than dense refractory brick.",
        "Kenworks Ventures supplies ceramic fiber board at 320 kg/m³ in the standard 600×300×50mm size, with strong dimensional stability and easy on-site machining. As a direct importer we keep board in stock for engineers and fabricators across Kenya. Share your furnace dimensions and target temperature and we will help you specify the correct board grade and quantity."]),
 dict(slug="rockwool-roll", name="Rockwool Roll / Blanket", div="insulation", temp="1000°C", img="rockwool-roll",
  h1="Rockwool Insulation Roll & Blanket in Nairobi, Kenya",
  title="Rockwool Insulation Roll in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy rockwool (mineral wool) roll and blanket in Nairobi, Kenya. 1000°C, 100 kg/m³, wire-mesh reinforced. Direct importer & supplier — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1000°C"),("Material","Basalt stone wool (mineral wool)"),("Density","100 kg/m³"),("Reinforcement","Galvanised / stainless steel wire mesh"),("Dimensions","6m × 1m × 50mm; 3m × 1m × 75mm; 3m × 1m × 100mm"),("Price","{{PRICE_PER_ROLL}} — request a quote")],
  apps=["Lagging of tanks, pipes and ducts","Boiler and furnace external insulation","Fire-rated wall and roof insulation","High-temperature industrial equipment"],
  copy=["Rockwool roll, also called mineral wool or stone wool, is a non-combustible insulation spun from molten basalt rock. Reinforced with steel wire mesh, it wraps tightly around tanks, pipes, ducts and boilers and holds up to continuous temperatures of 1000°C. It delivers thermal performance, fire resistance and useful sound absorption in a single material.",
        "Kenworks Ventures stocks wire-mesh rockwool blanket at 100 kg/m³ density in 50mm, 75mm and 100mm thicknesses. We are a direct importer, so industrial buyers in Nairobi and across East Africa get sharp pricing and reliable supply. Tell us the surface temperature and area to be lagged and we will recommend the right density and thickness."]),
 dict(slug="rockwool-batts", name="Rockwool Batts / Slabs", div="insulation", temp="1000°C", img="rockwool-batts",
  h1="Rockwool Batts & Slabs in Nairobi, Kenya",
  title="Rockwool Batts & Slabs in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy rockwool batts and slabs in Nairobi, Kenya. Rigid 1000°C panels, 50 kg/m³, 1.2×0.6m. Direct importer & supplier — same-day WhatsApp quotes from Kenworks Ventures.",
  specs=[("Max service temperature","1000°C"),("Material","Rigid basalt stone wool"),("Density","50 kg/m³"),("Dimensions","1.2m × 0.6m × 50mm; 1.2m × 0.6m × 100mm"),("Form","Rigid batt / slab"),("Price","{{PRICE_PER_PACK}} — request a quote")],
  apps=["Thermal and fire insulation of walls and roofs","Floor and partition insulation","Acoustic treatment of plant rooms","Industrial equipment panels"],
  copy=["Rockwool batts are rigid, pre-cut panels of basalt stone wool used for thermal, acoustic and fire protection in walls, roofs, floors and industrial equipment. They are non-combustible, dimensionally stable and easy to friction-fit between studs and joists, making them a practical choice for both buildings and plant rooms.",
        "Kenworks Ventures supplies rockwool slabs at 50 kg/m³ density in 50mm and 100mm thicknesses, sized 1.2m × 0.6m. As a direct importer we hold stock for contractors and facility teams across Kenya. Let us know whether your priority is fire rating, thermal value or sound control and we will match you to the right slab."]),
 dict(slug="preformed-rockwool-pipe", name="Preformed Rockwool Pipe Section", div="insulation", temp="1000°C", img="preformed-rockwool-pipe",
  h1="Preformed Rockwool Pipe Lagging in Nairobi, Kenya",
  title="Preformed Rockwool Pipe Section in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy preformed rockwool pipe sections for lagging in Nairobi, Kenya. 1000°C, 150 kg/m³, ½\"–6\" bore. Direct importer & supplier — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1000°C"),("Material","Preformed basalt stone wool"),("Density","150 kg/m³"),("Wall thickness","25mm and 50mm"),("Internal bore","½\", ¾\", 1\", 1.5\", 2\", 2.5\", 3\", 4\", 5\", 6\""),("Price","{{PRICE_PER_SECTION}} — request a quote")],
  apps=["Lagging of steam and hot-water pipes","Chiller and chilled-water pipe insulation","Process and waste pipe lagging","Solar hot-water pipe insulation"],
  copy=["Preformed rockwool pipe sections are rigid, cylindrical shells of stone wool moulded to fit standard pipe bores. They snap straight onto hot or cold lines for fast, clean lagging that cuts energy loss and protects against burns. Rated to 1000°C, they suit steam, hot-water, chiller and process piping alike.",
        "Kenworks Ventures stocks preformed sections at 150 kg/m³ density in 25mm and 50mm wall thickness, covering bores from ½ inch up to 6 inches. As a direct importer we can supply matched sections and aluminium cladding for a complete lagging job. Send us your pipe schedule and run lengths for an accurate quote."]),
 dict(slug="fiberglass-roll", name="Fiberglass (Glasswool) Roll", div="insulation", temp="350–450°C", img="fiberglass-roll",
  h1="Fiberglass Insulation Roll in Nairobi, Kenya",
  title="Fiberglass (Glasswool) Roll in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy fiberglass / glasswool insulation roll in Nairobi, Kenya. 350–450°C, 24 kg/m³, foil-faced options. Direct importer & supplier — same-day WhatsApp quotes.",
  specs=[("Max service temperature","350–450°C"),("Material","Glasswool (fiberglass)"),("Density","24 kg/m³"),("Dimensions","20m × 1.2m × 50mm; 10m × 1.2m × 50mm; 10m × 1.2m × 100mm"),("Facing","Plain or aluminium foil"),("Price","{{PRICE_PER_ROLL}} — request a quote")],
  apps=["Roof and ceiling insulation","HVAC duct wrap","Wall and partition insulation","Acoustic lining"],
  copy=["Fiberglass insulation roll, or glasswool, is a lightweight, economical thermal and acoustic material made from fine glass fibers. It installs quickly between studs, joists and over ductwork, and is non-combustible. Available plain or with an aluminium foil vapour facing, it is widely used for roofing, ducting, HVAC and wall insulation.",
        "Kenworks Ventures supplies glasswool at 24 kg/m³ density in 50mm and 100mm thicknesses, with or without foil. As a direct importer we keep rolls in stock for builders and HVAC contractors across Kenya. Tell us whether you need a vapour barrier and we will quote the right facing and roll size for your project."]),
 dict(slug="fiberglass-batts", name="Fiberglass (Glasswool) Batts", div="insulation", temp="350–450°C", img="fiberglass-batts",
  h1="Fiberglass Insulation Batts in Nairobi, Kenya",
  title="Fiberglass (Glasswool) Batts in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy fiberglass / glasswool batts in Nairobi, Kenya. 350–450°C, 32 kg/m³, 1.2×0.6m. Direct importer & supplier — same-day WhatsApp quotes from Kenworks Ventures.",
  specs=[("Max service temperature","350–450°C"),("Material","Glasswool (fiberglass)"),("Density","32 kg/m³"),("Dimensions","1.2m × 0.6m × 50mm; 1.2m × 0.6m × 100mm"),("Form","Pre-cut batt / slab"),("Price","{{PRICE_PER_PACK}} — request a quote")],
  apps=["Walls, ceilings and partitions","Suspended ceiling tiles backing","HVAC and acoustic insulation","Commercial fit-outs"],
  copy=["Fiberglass batts are pre-cut glasswool panels engineered for fast thermal and acoustic insulation of walls, ceilings, partitions and HVAC systems. They are lightweight, non-combustible and friction-fit between framing, making them a clean choice for commercial and residential fit-outs.",
        "Kenworks Ventures supplies fiberglass batts at 32 kg/m³ density in 50mm and 100mm thicknesses, sized 1.2m × 0.6m. As a direct importer we hold stock for contractors across Kenya and East Africa. Share your wall or ceiling area and target sound or thermal performance for a same-day quote."]),
 dict(slug="armaflex", name="Armaflex Insulation (Sheet & Roll)", div="insulation", temp="−40 to 120°C", img="armaflex",
  h1="Armaflex Insulation in Nairobi, Kenya",
  title="Armaflex Insulation Sheet & Roll in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy Armaflex closed-cell insulation in Nairobi, Kenya. −40 to 120°C, 80 kg/m³, plain or foil with adhesive. Direct importer & supplier — same-day WhatsApp quotes.",
  specs=[("Service range","−40°C to 120°C"),("Material","Closed-cell elastomeric foam (NBR/EPDM)"),("Density","80 kg/m³"),("Thermal conductivity","≈ 0.033–0.038 W/m·K"),("Dimensions","8m×1m×25mm; 10m×1m×19mm; 14m×1m×12.5mm"),("Options","Plain, or foil-faced with self-adhesive"),("Price","{{PRICE_PER_ROLL}} — request a quote")],
  apps=["Chilled-water and refrigeration lines","HVAC ducting and pipework","Condensation and corrosion-under-insulation control","Plumbing and solar systems"],
  copy=["Armaflex is a flexible, closed-cell elastomeric foam with a built-in vapour barrier, engineered to stop condensation and heat loss on cold and chilled systems. With low thermal conductivity and a service range of −40°C to 120°C, it is the standard for HVAC, refrigeration and chilled-water pipework where moisture control matters.",
        "Kenworks Ventures stocks Armaflex sheet and roll at 80 kg/m³ density, in plain and foil-faced self-adhesive versions across several thicknesses. As a direct importer we supply matched Armaflex tape for sealed seams. Tell us your pipe sizes and the lowest operating temperature and we will quote the right wall thickness."]),
 dict(slug="calcium-silicate", name="Calcium Silicate Board", div="insulation", temp="1100°C", img="calcium-silicate",
  h1="Calcium Silicate Board in Nairobi, Kenya",
  title="Calcium Silicate Board in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy calcium silicate board in Nairobi, Kenya. High-strength 1100°C insulation board, 600×300×50mm. Direct importer & supplier — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1100°C"),("Material","Calcium silicate with reinforcing fibers"),("Dimensions","600mm × 300mm × 50mm"),("Properties","Water-resistant, fire-resistant, dimensionally stable"),("Form","Rigid board"),("Price","{{PRICE_PER_BOARD}} — request a quote")],
  apps=["Furnace and boiler hot-face insulation","Fire-rated wall and ceiling panels","Pipe and equipment insulation","High-temperature load-bearing insulation"],
  copy=["Calcium silicate board is a high-strength, rigid insulation made from silica, lime and reinforcing fibers. It withstands high temperatures without warping, cracking or shrinking, is non-combustible, and resists moisture, mould and decay — a dependable hot-face board for furnaces, boilers and fire-rated construction up to 1100°C.",
        "Kenworks Ventures supplies calcium silicate board in the standard 600×300×50mm size, easy to cut and install. As a direct importer we keep board in stock for industrial and construction clients across Kenya. Share your operating temperature and panel area and we will confirm board quantity and any back-up insulation you need."]),
 dict(slug="vermiculite", name="Vermiculite Insulation", div="insulation", temp="1100°C", img="vermiculite",
  h1="Vermiculite Insulation in Nairobi, Kenya",
  title="Vermiculite Insulation in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy vermiculite insulation in Nairobi, Kenya. Non-combustible loose-fill, up to 1100°C, medium & large grade, 10kg bags. Direct importer & supplier — WhatsApp quotes.",
  specs=[("Max service temperature","1100°C"),("Material","Exfoliated vermiculite (mica mineral)"),("Thermal conductivity","≈ 0.06–0.09 W/m·K"),("Grades","Medium grade, large grade"),("Packing","10 kg bag"),("Fire class","Class A, non-combustible"),("Price","{{PRICE_PER_BAG}} — request a quote")],
  apps=["Loose-fill insulation for masonry and chimney flues","Fireproofing and high-temperature linings","Refractory and concrete mixes","Soil conditioning and seed germination"],
  copy=["Vermiculite is a lightweight, non-combustible mineral expanded by heat into a loose-fill insulation. It offers strong thermal performance and fire resistance up to 1100°C, is chemically inert, and resists moisture and mould. Pour it into masonry cavities, chimney flues and refractory mixes, or use it for fireproofing and high-temperature linings.",
        "Kenworks Ventures stocks vermiculite in medium and large grade, supplied in 10kg bags. As a direct importer we supply both construction and industrial users across Kenya, including for refractory castable and concrete blends. Tell us your application and volume and we will recommend the grade and quantity."]),
 dict(slug="styrofoam", name="Styrofoam (Polystyrene) Insulation", div="insulation", temp="—", img="styrofoam",
  h1="Styrofoam (Polystyrene) Insulation Boards in Nairobi, Kenya",
  title="Styrofoam Polystyrene Insulation in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy styrofoam / polystyrene (EPS) insulation boards in Nairobi, Kenya. 1.2×1.2m, ½\"–4\" thick. Direct importer & supplier — same-day WhatsApp quotes.",
  specs=[("Material","Expanded polystyrene (EPS)"),("Standard size","1.2m × 1.2m (4ft × 4ft)"),("Thicknesses","½\", 1\", 2\", 3\", 4\""),("Forms","Flexible and rigid sheets"),("Properties","Low conductivity, moisture-resistant, lightweight"),("Price","{{PRICE_PER_SHEET}} — request a quote")],
  apps=["Roof, wall and floor insulation","Cold rooms and packaging","Expansion joint filler","Underlay for laminated flooring"],
  copy=["Styrofoam, or expanded polystyrene (EPS), is a lightweight, cost-effective insulation that traps air in closed cells to block conduction and convection. It resists moisture, holds its shape and is easy to cut, making it a versatile choice for roofs, walls, floors, cold rooms, packaging and expansion-joint filling.",
        "Kenworks Ventures supplies styrofoam in the standard 1.2m × 1.2m sheet across thicknesses from ½ inch to 4 inches, in flexible and rigid forms. As a direct importer we keep sheets in stock for builders and cold-chain clients across Kenya. Tell us your thickness and quantity for a same-day price."]),
 dict(slug="pe-roof", name="Polyethylene Roof Insulation", div="insulation", temp="—", img="pe-roof",
  h1="Polyethylene Reflective Roof Insulation in Nairobi, Kenya",
  title="Polyethylene Roof Insulation in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy double-sided reflective polyethylene roof insulation in Nairobi, Kenya. Radiant heat & moisture barrier, 40m×1.5m rolls. Direct importer & supplier — WhatsApp quotes.",
  specs=[("Material","Closed-cell polyethylene foam, double-laminated reflective foil"),("Type","Double-sided reflective roof insulation"),("Dimensions","40m × 1.5m × 2mm; 40m × 1.5m × 3mm; 50m × 1.2m × 10mm"),("Function","Radiant heat barrier + moisture barrier"),("Price","{{PRICE_PER_ROLL}} — request a quote")],
  apps=["Under-roof radiant heat barrier","Warehouse and factory metal roofs","Cold storage facilities","Ceiling and wall reflective insulation"],
  copy=["Polyethylene roof insulation is a double-sided reflective foil bonded to a closed-cell foam core. It reflects radiant heat, blocks moisture and dampens noise from rain and wind, protecting roof spaces from heat build-up and condensation. Lightweight and flexible, it installs quickly under metal roofing sheets and ceilings.",
        "Kenworks Ventures supplies double-laminated PE roof insulation in 2mm, 3mm and 10mm thicknesses on long rolls. As a direct importer we keep stock for roofers and industrial builders across Kenya — ideal for warehouses, factories and cold stores. Send us your roof area for a roll count and quote."]),
 dict(slug="alu-foil", name="Aluminium Foil FSK & Insulation Tapes", div="insulation", temp="—", img="alu-foil",
  h1="Aluminium Foil FSK & Insulation Tapes in Nairobi, Kenya",
  title="Aluminium Foil FSK & Insulation Tapes in Kenya | Price — Kenworks Ventures",
  meta="Buy aluminium foil FSK facing, thermal foil tape and butyl waterproof tape in Nairobi, Kenya. Vapour barrier & sealing. Direct importer — same-day WhatsApp quotes.",
  specs=[("FSK foil","Aluminium foil + fiberglass scrim + kraft, 100m × 1.2m wide"),("Aluminium thermal tape",'2" × 18m and 3" × 18m'),("Butyl waterproof tape","5m × 5cm and 10m × 10cm"),("Function","Vapour barrier, radiant reflection, sealing"),("Price","{{PRICE_PER_UNIT}} — request a quote")],
  apps=["HVAC duct insulation facing","Roof and wall vapour barrier","Sealing insulation seams and joints","Waterproofing irregular and damp surfaces"],
  copy=["Aluminium Foil FSK is a reflective facing of foil reinforced with fiberglass scrim and kraft paper that acts as a vapour barrier and radiant heat reflector for duct, roof and wall insulation. Alongside it we stock aluminium thermal foil tape and butyl waterproof sealing tape for finishing and sealing insulation systems.",
        "Kenworks Ventures supplies FSK foil in 100m × 1.2m rolls, plus 2\" and 3\" thermal foil tapes and butyl tapes in two widths. As a direct importer we keep these accessories in stock to complete any lagging or duct-wrap job. Tell us your application and we will quote the right facing and tape."]),
 dict(slug="ceramic-rope", name="Ceramic Fiber Rope", div="refractory", temp="1260°C", img="ceramic-rope",
  h1="Ceramic Fiber Rope in Nairobi, Kenya",
  title="Ceramic Fiber Rope in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy non-asbestos ceramic fiber rope in Nairobi, Kenya. 1260°C round & square, 6–50mm. Furnace and kiln door sealing. Direct importer — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1260°C"),("Material","Non-asbestos ceramic fiber"),("Density","500–700 kg/m³"),("Profiles","Round and square"),("Thickness","6, 8, 10, 12, 14, 16, 19, 25, 32, 38, 45, 50 mm"),("Price","{{PRICE_PER_METRE}} — request a quote")],
  apps=["Furnace and kiln door sealing","Boiler and stove gaskets","Expansion-joint packing","High-temperature gap sealing"],
  copy=["Ceramic fiber rope is a heat-resistant, flexible seal braided from non-asbestos ceramic fibers. It seals furnace and kiln doors, boiler access points and expansion joints, holding up to continuous service at 1260°C. Available in round and square profiles, it compresses to fill gaps and stays resilient through thermal cycling.",
        "Kenworks Ventures stocks ceramic rope in round and square profiles from 6mm up to 50mm thick, at 500–700 kg/m³ density. As a direct importer we cut to the lengths you need. Tell us the gap width and profile and we will recommend the right rope size and quantity."]),
 dict(slug="ceramic-cloth", name="Ceramic Fiber Cloth", div="refractory", temp="1260°C", img="ceramic-cloth",
  h1="Ceramic Fiber Cloth in Nairobi, Kenya",
  title="Ceramic Fiber Cloth (Plain & Foil) in Kenya | Price — Kenworks Ventures",
  meta="Buy non-asbestos ceramic fiber cloth in Nairobi, Kenya. 1260°C woven fabric, plain or foil-backed, 30m×1m×3mm. Direct importer — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1260°C"),("Material","Woven non-asbestos ceramic fiber yarn"),("Density","500–720 kg/m³"),("Dimensions","30m × 1m × 3mm"),("Options","Plain, or aluminium foil-backed"),("Price","{{PRICE_PER_METRE}} — request a quote")],
  apps=["Heat shielding and welding curtains","Expansion joints","Exhaust and furnace insulation wrapping","High-temperature gaskets"],
  copy=["Ceramic fiber cloth is a high-temperature woven fabric made from ceramic fiber yarn, used for heat shielding, expansion joints and fire protection. The foil-backed version reflects radiant heat for improved energy efficiency in furnace insulation, heat shields and exhaust systems. Both resist heat, thermal shock and chemical attack at up to 1260°C.",
        "Kenworks Ventures supplies ceramic cloth in plain and foil-backed forms, 30m × 1m × 3mm, with custom lengths available. As a direct importer we keep it in stock for fabricators and maintenance teams across Kenya. Tell us whether you need radiant reflection and we will quote plain or foil-backed cloth."]),
 dict(slug="ceramic-tape", name="Ceramic Fiber Tape", div="refractory", temp="1260°C", img="ceramic-tape",
  h1="Ceramic Fiber Tape in Nairobi, Kenya",
  title="Ceramic Fiber Tape in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy non-asbestos ceramic fiber tape in Nairobi, Kenya. 1260°C sealing tape, 10m×50mm×3mm, custom lengths. Direct importer — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1260°C"),("Material","Non-asbestos ceramic fiber"),("Density","500–550 kg/m³"),("Dimensions","10m × 50mm × 3mm"),("Lengths","Custom lengths available"),("Price","{{PRICE_PER_ROLL}} — request a quote")],
  apps=["Wrapping pipes and flanges","Sealing furnace doors","Insulating high-temperature equipment","Cable and joint protection"],
  copy=["Ceramic fiber tape is a flexible, heat-resistant sealing tape made from non-asbestos ceramic fibers. It wraps and seals pipes, flanges and furnace doors, and insulates high-temperature equipment at continuous service up to 1260°C. Its woven construction stays intact through thermal cycling and resists chemical attack.",
        "Kenworks Ventures supplies ceramic tape in 10m × 50mm × 3mm rolls with custom lengths available on request. As a direct importer we keep it in stock for plant maintenance across Kenya. Tell us the diameter to be wrapped and length needed for a quick quote."]),
 dict(slug="ceramic-yarn", name="Ceramic Fiber Yarn / Thread", div="refractory", temp="1260°C", img="ceramic-yarn",
  h1="Ceramic Fiber Yarn & Thread in Nairobi, Kenya",
  title="Ceramic Fiber Yarn / Thread in Kenya | Price — Kenworks Ventures",
  meta="Buy non-asbestos ceramic fiber yarn and thread in Nairobi, Kenya. 1260°C twisted fiber for stitching and packing. Direct importer — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1260°C"),("Material","Twisted non-asbestos ceramic fiber"),("Properties","High tensile strength, low thermal conductivity"),("Use","Stitching, gasketing, packing, reinforcement"),("Price","{{PRICE_PER_KG}} — request a quote")],
  apps=["Stitching insulation products","Gasketing and gland packing","Reinforcing ceramic textiles","Furnace and kiln applications"],
  copy=["Ceramic fiber yarn, or thread, is a high-temperature twisted fiber engineered for thermal insulation, sealing and reinforcement. With good tensile strength and low thermal conductivity at up to 1260°C, it is used for stitching insulation products, gasketing, packing and reinforcing ceramic textiles in furnace applications.",
        "Kenworks Ventures supplies ceramic yarn and thread for industrial sewing and packing across Kenya. As a direct importer we keep it in stock alongside our ceramic cloth, tape and rope range. Tell us your application and quantity for a same-day quote."]),
 dict(slug="gland-packing", name="Gland Packing (PTFE / Aramid / Graphited)", div="refractory", temp="High temp", img="gland-packing",
  h1="Gland Packing in Nairobi, Kenya",
  title="Gland Packing — PTFE, Aramid & Graphited in Kenya | Price — Kenworks Ventures",
  meta="Buy gland packing in Nairobi, Kenya — PTFE, aramid/Kevlar and graphited packing for valves and pumps on steam and hot fluids. Direct importer — WhatsApp quotes.",
  specs=[("Types","PTFE, aramid/Kevlar, graphited/aramid"),("Use","Valve and pump shaft sealing"),("Media","Steam, hot water, oils and process fluids"),("Temperature rating","{{MAX_TEMP_BY_GRADE}}"),("Sizes","{{SIZES}}"),("Price","{{PRICE_PER_KG}} — request a quote")],
  apps=["Valve stem sealing","Centrifugal and reciprocating pump shafts","Steam and hot-fluid systems","General industrial gland sealing"],
  copy=["Gland packing seals the moving shafts of valves and pumps against leakage of steam, hot water and process fluids. Kenworks Ventures stocks PTFE, aramid/Kevlar and graphited packing grades, each suited to different pressures, speeds and media, so you can match the packing to the duty rather than compromise on a single type.",
        "As a direct importer we supply gland packing by the coil and can advise on the right cross-section and grade for your equipment. Share the shaft size, media and temperature and we will recommend a packing type and quote it. (Some temperature and size values are marked as placeholders pending confirmation of the grades you stock.)"]),
 dict(slug="steam-gasket", name="Steel Metallic Steam Gasket (Superlite 5000)", div="refractory", temp="500–650°C", img="steam-gasket",
  h1="Metallic Steam Gaskets in Nairobi, Kenya",
  title="Steel Metallic Steam Gaskets (Superlite 5000) in Kenya | Price — Kenworks Ventures",
  meta="Buy steel metallic steam gaskets (Superlite 5000) in Nairobi, Kenya. 500–650°C, sheet 1.5–6mm. High-pressure flange sealing. Direct importer — WhatsApp quotes.",
  specs=[("Max service temperature","500–650°C (by steel grade)"),("Brand","Superlite 5000"),("Material","Stainless / carbon steel"),("Sheet sizes","1500×1000mm in 1.5, 2, 2.5, 3, 4, 5, 6 mm"),("Properties","High mechanical strength, chemical and oxidation resistance"),("Price","{{PRICE_PER_SHEET}} — request a quote")],
  apps=["High-pressure steam flange joints","Oil, gas and petrochemical piping","Power-generation sealing","High-temperature process systems"],
  copy=["Steel metallic steam gaskets are precision sealing components for high-pressure, high-temperature flange and piping systems. Made from stainless or carbon steel, they withstand thermal cycling and aggressive media in steam, oil, gas and power applications, with service temperatures from 500°C up to 650°C depending on grade.",
        "Kenworks Ventures supplies Superlite 5000 metallic steel gasket sheet from 1.5mm to 6mm thickness in 1500 × 1000mm sheets, ready to cut to your flange pattern. As a direct importer we hold stock for industrial maintenance across Kenya. Send your flange size and pressure class for a quote."]),
 dict(slug="millboard", name="Asbestos Millboard", div="refractory", temp="1100°C", img="millboard",
  h1="Millboard (Heat-Resistant Gasket Board) in Nairobi, Kenya",
  title="Millboard Heat-Resistant Gasket Board in Kenya | Price — Kenworks Ventures",
  meta="Buy heat-resistant millboard in Nairobi, Kenya. Rigid insulation panel up to 1100°C, 1×1m, 3–12mm. Fire doors, gaskets, furnace linings. Direct importer — WhatsApp quotes.",
  specs=[("Max service temperature","1100°C"),("Material","Compressed mineral / refractory fibre"),("Thermal conductivity","≈ 0.06–0.12 W/m·K"),("Dimensions","1m × 1m in 3, 4, 5, 6, 8, 10, 12 mm"),("Properties","Non-combustible, thermal-shock resistant"),("Price","{{PRICE_PER_SHEET}} — request a quote")],
  apps=["Fire doors and heat shields","Cut gaskets and jointing","Furnace and boiler linings","Industrial heat containment"],
  copy=["Millboard is a rigid, compressed-fibre insulation panel that provides effective thermal insulation up to 1100°C with strong mechanical strength and thermal-shock resistance. Non-combustible and easy to cut, it is widely used for fire doors, furnace linings, boiler insulation and cut gaskets in industrial heat-containment systems.",
        "Kenworks Ventures supplies millboard in 1m × 1m sheets across thicknesses from 3mm to 12mm. As a direct importer we keep the full thickness range in stock for fabricators and maintenance teams across Kenya. Tell us your thickness and quantity for a same-day price."]),
 dict(slug="knauf-acoustic", name="Knauf Acoustic Mineral Wool Roll", div="insulation", temp="—", img="knauf-acoustic",
  h1="Acoustic Mineral Wool Insulation in Nairobi, Kenya",
  title="Knauf Acoustic Mineral Wool Roll in Kenya | Price — Kenworks Ventures",
  meta="Buy acoustic mineral wool insulation rolls in Nairobi, Kenya for soundproofing studios, walls and ducts. Direct importer & supplier — same-day WhatsApp quotes.",
  specs=[("Material","Acoustic mineral wool"),("Use","Sound absorption and noise control"),("Density","{{DENSITY}}"),("Dimensions","{{DIMENSIONS}}"),("Price","{{PRICE_PER_ROLL}} — request a quote")],
  apps=["Recording studios and media rooms","Partition and wall soundproofing","Plant-room and duct noise control","Conference and church halls"],
  copy=["Acoustic mineral wool roll is a dense insulation engineered for sound absorption in studios, partitions, ducts and plant rooms. Its fibrous structure traps sound energy to cut noise transfer and reduce echo, while remaining non-combustible — a dual thermal and acoustic solution for demanding spaces.",
        "Kenworks Ventures supplies acoustic mineral wool for soundproofing projects across Kenya, and has completed acoustic insulation of conference halls, church halls and call centres. As a direct importer we hold stock for fast turnaround. Tell us your room dimensions and noise target for a tailored quote. (Density and dimensions are marked as placeholders pending your confirmed stock spec.)"]),
 dict(slug="acoustic-foam", name="Acoustic Foam Wedges & Panels", div="insulation", temp="—", img="acoustic-foam",
  h1="Acoustic Foam Wedges & Panels in Nairobi, Kenya",
  title="Acoustic Foam Wedges & Panels in Kenya | Price — Kenworks Ventures",
  meta="Buy acoustic foam wedges and panels in Nairobi, Kenya for echo control and soundproofing. Direct importer & supplier — same-day WhatsApp quotes from Kenworks Ventures.",
  specs=[("Material","Profiled acoustic foam"),("Forms","Wedge panels and flat panels"),("Use","Echo reduction and noise control"),("Dimensions","{{DIMENSIONS}}"),("Price","{{PRICE_PER_PANEL}} — request a quote")],
  apps=["Recording and broadcast studios","Home theatres and media rooms","Offices and meeting rooms","Echo control in halls"],
  copy=["Acoustic foam wedges and panels are profiled sound-absorbing tiles that tame echo and reverberation in studios, theatres and meeting rooms. The wedge profile increases surface area to absorb mid and high frequencies, improving speech clarity and recording quality.",
        "Kenworks Ventures supplies acoustic foam wedges and panels for soundproofing projects across Kenya. As a direct importer we keep stock for studios and commercial fit-outs. Tell us your wall area and the type of room and we will recommend coverage and quote it. (Panel dimensions are a placeholder pending confirmation of your stocked sizes.)"]),
 dict(slug="firebrick-40", name="40% Alumina Refractory Firebrick", div="refractory", temp="1600°C", img="firebrick-40",
  h1="40% Alumina Firebricks in Nairobi, Kenya",
  title="40% Alumina Refractory Firebricks in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy 40% alumina refractory firebricks in Nairobi, Kenya. 1600°C, 230×115×75mm, standard, arch, slab & split shapes. Direct importer — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1600°C"),("Alumina content","≈ 40% Al₂O₃"),("Standard size","230mm × 115mm × 75mm"),("Shapes","Standard, side arch (75/63mm), end arch (75/65mm), slab (600×300×75mm), split (230×115×25mm)"),("Price","{{PRICE_PER_BRICK}} — request a quote")],
  apps=["Furnace and kiln linings","Fireplaces and pizza ovens","Boiler and incinerator linings","General high-temperature construction"],
  copy=["40% alumina firebricks are general-duty refractory blocks that balance high-temperature resistance, thermal stability and durability. Rated to 1600°C, they are the workhorse brick for furnace and kiln linings, fireplaces, boilers and incinerators, and are available in standard, arch, slab and split shapes to suit curved and flat builds.",
        "Kenworks Ventures is one of Kenya's main refractory distributors and stocks 40% alumina firebricks in the full shape range at 230×115×75mm standard size. We import directly and also export to Uganda, Tanzania and Rwanda. Send your brick count and shapes for a competitive quote."]),
 dict(slug="firebrick-70", name="70% Alumina Refractory Firebrick", div="refractory", temp="1800°C", img="firebrick-70",
  h1="70% Alumina Firebricks in Nairobi, Kenya",
  title="70% Alumina High-Duty Firebricks in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy 70% alumina firebricks in Nairobi, Kenya. High-duty 1750–1800°C, slag-resistant, 5.2kg, 230×115×75mm. Direct importer — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1750–1800°C"),("Alumina content","≈ 70% Al₂O₃"),("Standard size","230mm × 115mm × 75mm"),("Weight","5.2 kg"),("Properties","High refractoriness, slag and chemical resistance, load-bearing"),("Price","{{PRICE_PER_BRICK}} — request a quote")],
  apps=["Steel furnaces and ladles","High-temperature kilns","Boilers and incinerators","Severe slag and chemical-attack zones"],
  copy=["70% alumina firebricks are high-duty refractory bricks with roughly 70% Al₂O₃, giving excellent thermal stability, high refractoriness up to 1800°C, strong slag and chemical resistance and good load-bearing strength at temperature. They are the right choice for steel furnaces, ladles, high-temperature kilns and incinerators under severe thermal and chemical conditions.",
        "Kenworks Ventures stocks 70% alumina brick at the standard 230×115×75mm size, 5.2kg each, and exports high-alumina firebrick across East Africa. As a direct importer we keep severe-duty brick on the shelf for steel and process plants. Tell us your lining area and shape requirements for a quote."]),
 dict(slug="zirconia", name="Zirconia Refractory Firebrick", div="refractory", temp="2000°C", img="zirconia",
  h1="Zirconia Refractory Firebricks in Nairobi, Kenya",
  title="Zirconia Refractory Firebricks in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy zirconia refractory firebricks in Nairobi, Kenya. Up to 2000°C, 230×115×38mm, 2.2kg. Glass furnaces and steel ladles. Direct importer — WhatsApp quotes.",
  specs=[("Max service temperature","2000°C"),("Material","Zirconium-oxide refractory"),("Standard size","230mm × 115mm × 38mm"),("Weight","2.2 kg"),("Properties","Outstanding thermal stability and chemical resistance"),("Price","{{PRICE_PER_BRICK}} — request a quote")],
  apps=["Glass-melting furnaces","Steel ladles","High-temperature kilns","Extreme-duty hot zones"],
  copy=["Zirconia firebricks are the highest-rated brick we stock, made with zirconium oxide for outstanding thermal stability and chemical resistance at temperatures up to 2000°C. They are used where ordinary high-alumina brick reaches its limit — glass-melting furnaces, steel ladles and the hottest zones of industrial kilns.",
        "Kenworks Ventures supplies zirconia firebrick at 230×115×38mm, 2.2kg each, for glass and steel producers across Kenya and the region. As a direct importer we can source matched extreme-duty refractories for the same build. Tell us your hot-zone temperature and brick count for a quote."]),
 dict(slug="insulating-brick", name="Insulating Refractory Firebrick", div="refractory", temp="High temp", img="insulating-brick",
  h1="Insulating Firebricks in Nairobi, Kenya",
  title="Insulating Refractory Firebricks in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy lightweight insulating firebricks in Nairobi, Kenya. Low-density, low-conductivity, 230×115×75mm, 2kg. Cuts kiln fuel use. Direct importer — WhatsApp quotes.",
  specs=[("Type","Lightweight insulating firebrick (IFB)"),("Standard size","230mm × 115mm × 75mm"),("Weight","2 kg"),("Properties","Low density, low thermal conductivity, good thermal-shock resistance"),("Max service temperature","{{MAX_TEMP}}"),("Price","{{PRICE_PER_BRICK}} — request a quote")],
  apps=["Back-up insulation behind dense brick","Kilns, furnaces and pizza ovens","Chimneys and thermal processing units","Fuel-saving hot-face in low-abrasion zones"],
  copy=["Insulating firebricks are lightweight, low-density bricks with low thermal conductivity and good thermal-shock resistance. By cutting heat loss through furnace and kiln walls they reduce fuel consumption, and at around 2kg each they are far lighter to handle and build with than dense refractory brick.",
        "Kenworks Ventures stocks insulating firebrick at the standard 230×115×75mm size for kilns, furnaces, ovens, chimneys and thermal processing units across Kenya. As a direct importer we pair them with dense hot-face brick for efficient lining designs. Share your wall build-up for a quote. (Maximum service temperature is a placeholder pending the exact grade you require.)"]),
 dict(slug="acid-brick", name="Acid-Resistant Brick & Tile", div="refractory", temp="Acid-proof", img="acid-brick",
  h1="Acid-Resistant Bricks & Tiles in Nairobi, Kenya",
  title="Acid-Resistant Bricks & Tiles in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy acid-resistant bricks and tiles in Nairobi, Kenya. Corrosion-proof lining for chemical and acid environments, 230×115×38mm. Direct importer — WhatsApp quotes.",
  specs=[("Material","Acid-resistant ceramic"),("Standard size","230mm × 115mm × 38mm"),("Resistance","Corrosion, acid and chemical attack"),("Standard","{{STANDARD}}"),("Price","{{PRICE_PER_BRICK}} — request a quote")],
  apps=["Acid and chemical plant flooring","Effluent and process tank linings","Pickling and plating lines","Corrosive-environment construction"],
  copy=["Acid-resistant bricks and tiles are dense ceramic units engineered to resist corrosion and chemical attack. They line floors, tanks and channels in acid, plating and process environments where ordinary masonry would degrade, giving long service life in aggressive chemical exposure.",
        "Kenworks Ventures supplies acid-resistant brick and tile at 230×115×38mm for chemical and process plants across Kenya. As a direct importer we can also supply matching acid-resistant cement and mortar. Tell us your chemical exposure and area for a quote. (Compliance standard is a placeholder pending confirmation of the grade you require.)"]),
 dict(slug="maxheat-a", name="Maxheat A Refractory Castable", div="refractory", temp="1750°C", img="maxheat-a",
  h1="Maxheat A Refractory Castable Cement in Nairobi, Kenya",
  title="Maxheat A Refractory Castable (90% Alumina) in Kenya | Price — Kenworks Ventures",
  meta="Buy Maxheat A high-alumina refractory castable in Nairobi, Kenya. 90% alumina, service up to 1750°C, 25kg bags. Direct distributor — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1750°C (1750–1810°C)"),("Grade","High-alumina castable, 90% Al₂O₃"),("Binder","Calcium aluminate cement"),("Packing","25 kg bag"),("Properties","High strength, fast-setting, slag and heat resistant"),("Price","{{PRICE_PER_BAG}} — request a quote")],
  apps=["Furnace and kiln monolithic linings","Boiler and incinerator linings","Repairs and patching","High-temperature cast shapes"],
  copy=["Maxheat A is a high-purity, 90% alumina refractory castable rated for service up to 1750°C. It offers excellent mechanical strength, thermal stability and resistance to chemical attack, and sets fast for quick return to service — ideal for lining and repairing furnaces, kilns, boilers and incinerators.",
        "Kenworks Ventures is one of Kenya's main distributors of Maxheat castables, supplied in 25kg bags. As a direct distributor we keep Maxheat A in stock for refractory contractors and plant teams across Kenya and East Africa. Tell us the volume to be cast and we will work out bag quantity and quote it."]),
 dict(slug="maxheat-k", name="Maxheat K Refractory Castable", div="refractory", temp="1600°C", img="maxheat-k",
  h1="Maxheat K Refractory Castable Cement in Nairobi, Kenya",
  title="Maxheat K Refractory Castable (60% Alumina) in Kenya | Price — Kenworks Ventures",
  meta="Buy Maxheat K medium-duty refractory castable in Nairobi, Kenya. 60% alumina, service up to 1600°C, 25kg bags. Direct distributor — same-day WhatsApp quotes.",
  specs=[("Max service temperature","1600°C"),("Grade","Medium-duty castable, 60% Al₂O₃"),("Binder","Calcium aluminate cement"),("Packing","25 kg bag"),("Properties","Good thermal stability, strength and abrasion resistance"),("Price","{{PRICE_PER_BAG}} — request a quote")],
  apps=["General furnace and kiln linings","Fireplaces and ovens","Refractory repairs and patching","Medium-temperature cast shapes"],
  copy=["Maxheat K is a medium-duty refractory castable made from a blend of alumina and calcium aluminate cement, rated to 1600°C. It offers good thermal stability, strength and abrasion resistance, and is easy to mix and place — the practical choice for general-purpose refractory installations and repairs.",
        "Kenworks Ventures distributes Maxheat K in 25kg bags and keeps it in stock for refractory work across Kenya. As a direct distributor we supply it alongside Maxheat A and our mortar and Fondu range for complete linings. Send the cast volume for a bag count and quote."]),
 dict(slug="maxlyte", name="Maxlyte 11 Insulating Castable", div="refractory", temp="1300°C", img="maxlyte",
  h1="Maxlyte 11 Insulating Refractory Castable in Nairobi, Kenya",
  title="Maxlyte 11 Insulating Castable in Kenya | Spec & Price — Kenworks Ventures",
  meta="Buy Maxlyte 11 lightweight insulating refractory castable in Nairobi, Kenya. Up to 1300°C, low conductivity, energy-saving linings. Direct distributor — WhatsApp quotes.",
  specs=[("Max service temperature","1300°C"),("Type","Lightweight insulating castable"),("Binder","Calcium aluminate cement"),("Aggregate","Lightweight (perlite / vermiculite)"),("Properties","Low conductivity, hydraulic set, energy efficient"),("Price","{{PRICE_PER_BAG}} — request a quote")],
  apps=["Back-up insulating lining","Kilns, furnaces and incinerators","Energy-saving hot-face in low-abrasion zones","Cast and trowel insulating layers"],
  copy=["Maxlyte 11 is a lightweight insulating refractory castable rated for continuous service up to 1300°C. Built on lightweight aggregates and calcium aluminate cement, it delivers low thermal conductivity and strong adhesion, cutting heat loss and fuel use as a back-up or insulating layer in kilns, furnaces and incinerators.",
        "Kenworks Ventures distributes Maxlyte 11 for both cast and trowel application, supplied in bags. As a direct distributor we pair it with dense Maxheat castables for efficient, layered lining designs across Kenya. Tell us your lining build-up and volume for a quote."]),
 dict(slug="mortar", name="Refractory Mortar (Maxset 50 Fine)", div="refractory", temp="1500°C", img="mortar",
  h1="Refractory Mortar (Maxset 50 Fine) in Nairobi, Kenya",
  title="Refractory Mortar / Fire Clay (Maxset 50 Fine) in Kenya | Price — Kenworks Ventures",
  meta="Buy refractory mortar (Maxset 50 Fine fire clay) in Nairobi, Kenya. Bonds firebricks up to 1500°C. Direct distributor — same-day WhatsApp quotes from Kenworks Ventures.",
  specs=[("Max service temperature","1500°C"),("Brand","Maxset 50 Fine (also known as fire clay)"),("Material","Alumina and fireclay with calcium aluminate binder"),("Use","Laying and jointing firebricks"),("Properties","Good adhesion, plasticity and thermal stability"),("Price","{{PRICE_PER_BAG}} — request a quote")],
  apps=["Laying and jointing firebricks","Kilns, furnaces and fireplaces","Oven and incinerator construction","Refractory repairs"],
  copy=["Refractory mortar, branded Maxset 50 Fine and also known as fire clay, is a heat-resistant jointing material made from alumina and fireclay. It bonds firebricks and refractory components in kilns, furnaces, fireplaces and ovens, offering good adhesion, plasticity and thermal stability up to 1500°C.",
        "Kenworks Ventures distributes Maxset 50 Fine refractory mortar across Kenya, supplied ready to mix with water. As a direct distributor we supply it together with our 40% and 70% firebrick range for complete brick-and-mortar builds. Tell us your brick count for a mortar quantity and quote."]),
 dict(slug="fondu", name="Fondu Max-50 Cement", div="refractory", temp="1000°C", img="fondu",
  h1="Fondu Cement (Max-50) in Nairobi, Kenya",
  title="Fondu Max-50 Calcium Aluminate Cement in Kenya | Price — Kenworks Ventures",
  meta="Buy Fondu Max-50 calcium aluminate cement in Nairobi, Kenya. Fast-setting refractory binder up to 1000°C. Direct distributor — same-day WhatsApp quotes.",
  specs=[("Max service temperature","≈ 1000°C"),("Brand","Max-50"),("Material","Calcium aluminate cement (CAC)"),("Properties","Fast-setting, early strength, thermal-shock and abrasion resistant"),("Price","{{PRICE_PER_BAG}} — request a quote")],
  apps=["Rapid kiln and furnace repairs","High-strength refractory castables and mortars","Fireclay and insulating refractory mixes","Abrasion-resistant industrial floors"],
  copy=["Fondu Max-50 is a fast-setting calcium aluminate cement used as a high-performance refractory binder for service up to about 1000°C. It gains strength rapidly and resists thermal shock, chemical attack and abrasion, making it ideal where early return to service or heat exposure is required — kiln repairs, castables and industrial flooring.",
        "Kenworks Ventures distributes Fondu Max-50 across Kenya for refractory castables, mortars and fast repairs. As a direct distributor we supply it alongside Maxheat castables and aggregates for complete mixes. Tell us your application and volume for a quote."]),
 dict(slug="somafix", name="Somafix Heat-Resistant Sealant & Foam", div="refractory", temp="1500°C", img="somafix",
  h1="Somafix Heat-Resistant Sealant & PU Foam in Nairobi, Kenya",
  title="Somafix Sealant & PU Foam in Kenya | Price — Kenworks Ventures",
  meta="Buy Somafix heat-resistant silicone sealant (1500°C) and expanding PU foam in Nairobi, Kenya. Sealing, bonding and insulating. Direct importer — WhatsApp quotes.",
  specs=[("Heat-resistant sealant","Silicone, rated to 1500°C"),("PU foam","Expanding polyurethane foam"),("Use","Sealing, bonding, filling and insulating joints"),("Brand","Somafix"),("Price","{{PRICE_PER_UNIT}} — request a quote")],
  apps=["High-temperature joint sealing","Glazing, windows and doors","Expansion joints","Filling and insulating gaps and cavities"],
  copy=["Somafix supplies high-temperature silicone sealant rated to 1500°C plus expanding PU foam for sealing, bonding, filling and insulating. The sealant gives strong, flexible, weather- and heat-resistant joints, while the PU foam expands to fill voids and cavities with thermal and acoustic insulation and a tight air and moisture seal.",
        "Kenworks Ventures stocks Somafix heat-resistant sealant and PU foam for industrial and construction use across Kenya. As a direct importer we keep both in stock alongside our refractory range. Tell us your joint type and quantity for a quick quote."]),
 dict(slug="hv-mat", name="H.V Electrical Insulating Rubber Mat", div="electrical", temp="10–50 kV", img="hv-mat",
  h1="High-Voltage Electrical Insulating Mats in Nairobi, Kenya",
  title="H.V Electrical Insulating Rubber Mats (Class 0–4) in Kenya — Kenworks Ventures",
  meta="Buy high-voltage electrical insulating rubber mats in Nairobi, Kenya. Class 0–4 (10–50kV), ASTM D178 / IEC 61111, anti-slip. Direct importer — same-day WhatsApp quotes.",
  specs=[("Standards","ASTM D178, IEC 61111"),("Brand","Duratuf"),("Class 0","10 kV — 1m × 1m × 3.2mm"),("Class 1","20 kV — 1m × 1m × 4.8mm"),("Class 2","30 kV — 1m × 1m × 6.4mm"),("Class 3","40 kV — 1m × 1m × 9.5mm"),("Class 4","50 kV — 1m × 1m × 12.7mm"),("Roll length","10 metres"),("Price","{{PRICE_PER_METRE}} — request a quote")],
  apps=["Electrical substations","Switchrooms and control rooms","Transformer and panel maintenance areas","Workplace electrical safety compliance"],
  copy=["High-voltage electrical insulating rubber mats protect personnel from electric shock by providing a reliable, non-conductive barrier in front of live equipment. Duratuf mats meet ASTM D178 and IEC 61111, resist oils, chemicals and abrasion, and have an anti-slip textured surface for safe footing in substations and control rooms.",
        "Kenworks Ventures supplies the full class range — Class 0 (10kV) through Class 4 (50kV) — in 1m × 1m sheets and 10-metre rolls. As a direct importer we keep electrical safety matting in stock for utilities, industry and facilities across Kenya. Tell us the working voltage and we will recommend the correct class and quote it."]),
]

# ---------- shared snippets ----------
def emblem_defs():
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>'
            '<g id="kw-emblem">'
            '<g class="gear-navy" transform="translate(25 38)"><circle r="17" fill="none" stroke="var(--navy)" stroke-width="6.5" stroke-dasharray="5.2 4.4"/><circle r="13"/><circle r="6.4" fill="#fff"/><path d="M-2.4 1.6a4.6 4.6 0 1 1 4.2-2.1l3 3-1.7 1.7-3-3a4.6 4.6 0 0 1-2.5.4Z" fill="var(--navy)"/></g>'
            '<g class="gear-blue" transform="translate(45 21)"><circle r="12" fill="none" stroke="var(--blue)" stroke-width="5" stroke-dasharray="4.2 3.6"/><circle r="9"/><circle r="4.4" fill="#fff"/><path d="M-1.7 1.1a3.2 3.2 0 1 1 2.9-1.4l2 2-1.2 1.2-2-2a3.2 3.2 0 0 1-1.7.2Z" fill="var(--blue)"/></g>'
            '</g></defs></svg>')

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M.5 23.5l1.65-6a11.5 11.5 0 1 1 4.3 4.2L.5 23.5ZM6.7 19.4l.37.22a9.6 9.6 0 1 0-3.27-3.2l.24.38-.95 3.45 3.61-.85ZM17.6 14.1c-.24-.12-1.43-.7-1.65-.78-.22-.08-.38-.12-.54.12s-.62.78-.76.94-.28.18-.52.06a7.8 7.8 0 0 1-2.3-1.42 8.6 8.6 0 0 1-1.6-1.98c-.16-.28 0-.43.12-.55.11-.11.24-.28.36-.42a1.6 1.6 0 0 0 .24-.4.44.44 0 0 0 0-.42c-.06-.12-.54-1.3-.74-1.78s-.39-.4-.54-.41h-.46a.88.88 0 0 0-.64.3 2.68 2.68 0 0 0-.84 2c0 1.18.86 2.32.98 2.48s1.7 2.6 4.12 3.64a13.8 13.8 0 0 0 1.37.5 3.3 3.3 0 0 0 1.52.1c.46-.07 1.43-.58 1.63-1.15s.2-1.05.14-1.15-.22-.16-.46-.28Z"/></svg>'

def header_html(prefix=".."):
    return f'''<header id="top">
  <div class="wrap nav">
    <a href="{prefix}/index.html" class="logo" aria-label="Kenworks Ventures home">
      <svg class="emblem" viewBox="0 0 64 64" role="img" aria-label="Kenworks gear logo"><use href="#kw-emblem"/></svg>
      <span class="wordmark"><b>KENWORKS</b><small>Ventures Company Ltd</small></span>
    </a>
    <nav class="nav-links" id="navlinks">
      <a href="{prefix}/index.html#divisions">What We Do</a>
      <a href="{prefix}/index.html#products">Products</a>
      <a href="{prefix}/products/thermal-acoustic-insulation.html">Insulation</a>
      <a href="{prefix}/products/refractory-materials.html">Refractories</a>
      <a href="{prefix}/index.html#contact">Contact</a>
    </nav>
    <div class="nav-cta">
      <a href="tel:+254722706416" class="btn btn-ghost">0722 706 416</a>
      <a href="#quote" class="btn btn-primary">Get a Quote</a>
      <button class="nav-toggle" id="navToggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>'''

def footer_html(prefix=".."):
    return f'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a href="{prefix}/index.html" class="logo">
          <svg class="emblem" viewBox="0 0 64 64" aria-hidden="true"><use href="#kw-emblem"/></svg>
          <span class="wordmark"><b>KENWORKS</b><small style="color:#93a1cf">Ventures Company Ltd</small></span>
        </a>
        <p>Thermal &amp; acoustic insulation, refractory materials, electrical safety and generator servicing — supplied across Kenya and East Africa.</p>
        <p class="foot-tag">"Keeping you powered up — at all times."</p>
      </div>
      <div class="foot-col">
        <h5>Divisions</h5>
        <a href="{prefix}/products/thermal-acoustic-insulation.html">Thermal &amp; Acoustic Insulation</a>
        <a href="{prefix}/products/refractory-materials.html">Refractory Materials</a>
        <a href="{prefix}/products/electrical-power.html">Electrical Safety &amp; Power</a>
        <a href="{prefix}/index.html#products">All products</a>
      </div>
      <div class="foot-col">
        <h5>Company</h5>
        <a href="{prefix}/index.html#divisions">What we do</a>
        <a href="{prefix}/index.html#export">Export reach</a>
        <a href="{prefix}/index.html#why">Why us</a>
        <a href="{prefix}/index.html#quote">Get a quote</a>
      </div>
      <div class="foot-col">
        <h5>Contact</h5>
        <a href="tel:+254722706416">0722 706 416</a>
        <a href="tel:+254720119668">0720 119 668</a>
        <a href="mailto:info@kenworksventures.co.ke">info@kenworksventures.co.ke</a>
        <a href="https://maps.app.goo.gl/Bhz9fL1tdx7s6SwA9" target="_blank" rel="noopener">Old Enterprise Rd, Hema House,<br/>Godown 8, Industrial Area, Nairobi</a>
        <p>P.O. Box 22750-00400, Nairobi</p>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="yr"></span> Kenworks Ventures Company Limited. All rights reserved.</span>
      <span>Insulation · Refractories · Generator Service</span>
    </div>
  </div>
</footer>'''

def fab_mbar_html(wa_text):
    enc = wa_text.replace(" ", "%20").replace(",", "%2C").replace("'", "%27")
    return f'''<div class="fab">
  <a href="https://wa.me/{WA}?text={enc}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{WA_SVG}WhatsApp</a>
</div>
<div class="mbar">
  <a class="call" href="tel:+254722706416">Call Now</a>
  <a class="wa" href="https://wa.me/{WA}?text={enc}" target="_blank" rel="noopener">WhatsApp Quote</a>
</div>'''

COMMON_SCRIPT = '''<script>
  document.getElementById('yr').textContent = new Date().getFullYear();
  var hdr=document.getElementById('top');
  window.addEventListener('scroll',function(){hdr.classList.toggle('scrolled',window.scrollY>10)},{passive:true});
  var tgl=document.getElementById('navToggle'),lk=document.getElementById('navlinks');
  if(tgl){tgl.addEventListener('click',function(){var o=lk.classList.toggle('open');tgl.setAttribute('aria-expanded',o)});}
</script>'''

def esc(s): return html.escape(s, quote=True)

def product_url(p): return f"{BASE}/products/{p['slug']}.html"

def wa_link(text):
    enc = text.replace(" ", "%20").replace(",", "%2C").replace("'", "%27").replace(":", "%3A")
    return f"https://wa.me/{WA}?text={enc}"

def mailto_link(name):
    subj = f"Quote request: {name}".replace(" ", "%20").replace(":", "%3A")
    body = (f"Hello Kenworks Ventures,%0D%0A%0D%0A"
            f"I would like a quote for: {name}.%0D%0A%0D%0A"
            f"Quantity / size:%0D%0A"
            f"Delivery location:%0D%0A"
            f"My name:%0D%0A"
            f"Phone:%0D%0A%0D%0AThank you.").replace(" ", "%20")
    return f"mailto:{EMAIL}?subject={subj}&body={body}"

# ---------- product page ----------
def render_product(p):
    d = DIVISIONS[p["div"]]
    canonical = product_url(p)
    img_url = f"{BASE}/images/{p['img']}.jpg"
    wa = wa_link(f"Hi Kenworks, I would like a quote for: {p['name']}.")
    mailto = mailto_link(p["name"])
    spec_rows = "\n".join(
        f'        <tr><th scope="row">{esc(l)}</th><td>{esc(v)}</td></tr>' for l, v in p["specs"])
    apps = "\n".join(f"          <li>{esc(a)}</li>" for a in p["apps"])
    body = "\n".join(f"      <p>{esc(par)}</p>" for par in p["copy"])
    related = [q for q in PRODUCTS if q["div"] == p["div"] and q["slug"] != p["slug"]][:3]
    rel_cards = "\n".join(f'''        <a class="rel-card" href="{q['slug']}.html">
          <img src="../images/{q['img']}.jpg" alt="{esc(q['name'])} supplier in Nairobi, Kenya" loading="lazy" width="640" height="480" />
          <span>{esc(q['name'])}</span>
        </a>''' for q in related)

    product_jsonld = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": p["name"],
        "image": img_url,
        "description": p["meta"],
        "category": d["name"],
        "brand": {"@type": "Brand", "name": "Kenworks Ventures"},
        "offers": {
            "@type": "Offer",
            "priceCurrency": "KES",
            "availability": "https://schema.org/InStock",
            "url": canonical,
            "seller": {"@type": "Organization", "name": "Kenworks Ventures Company Limited"}
        }
    }
    import json
    breadcrumb_jsonld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": d["name"], "item": f"{BASE}/products/{d['slug']}.html"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": canonical},
        ]
    }
    org_jsonld = ORG_JSONLD

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["meta"])}" />
<meta name="theme-color" content="#0e1a52" />
<link rel="canonical" href="{canonical}" />
<meta property="og:type" content="product" />
<meta property="og:title" content="{esc(p["title"])}" />
<meta property="og:description" content="{esc(p["meta"])}" />
<meta property="og:image" content="{img_url}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:site_name" content="Kenworks Ventures" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{esc(p["title"])}" />
<meta name="twitter:description" content="{esc(p["meta"])}" />
<meta name="twitter:image" content="{img_url}" />
<script type="application/ld+json">{json.dumps(product_jsonld)}</script>
<script type="application/ld+json">{json.dumps(breadcrumb_jsonld)}</script>
<script type="application/ld+json">{json.dumps(org_jsonld)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="product.css" />
</head>
<body>
{emblem_defs()}
{header_html("..")}

<main>
  <nav class="breadcrumb wrap" aria-label="Breadcrumb">
    <a href="../index.html">Home</a> <span>›</span>
    <a href="{d['slug']}.html">{esc(d['name'])}</a> <span>›</span>
    <span aria-current="page">{esc(p['name'])}</span>
  </nav>

  <section class="prod-hero wrap">
    <div class="prod-hero-media">
      <img src="../images/{p['img']}.jpg" alt="{esc(p['name'])} supplier in Nairobi, Kenya — Kenworks Ventures" width="640" height="480" />
      <span class="temp-badge">{esc(p['temp']) if p['temp']!='—' else 'General use'}</span>
    </div>
    <div class="prod-hero-info">
      <span class="eyebrow">{esc(d['name'])}</span>
      <h1>{esc(p['h1'])}</h1>
      <p class="lead">{esc(p['copy'][0])}</p>
      <div class="cta-row">
        <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}Get a quote on WhatsApp</a>
        <a class="btn btn-ghost" href="{mailto}">Email this quote</a>
      </div>
      <p class="cta-sub">Or call the sales desk: <a href="tel:+254722706416">0722 706 416</a> · <a href="tel:+254720119668">0720 119 668</a></p>
    </div>
  </section>

  <section class="wrap prod-detail">
    <div class="prod-detail-main">
      <h2>{esc(p['name'])} — specifications</h2>
      <table class="spec-table">
        <tbody>
{spec_rows}
        </tbody>
      </table>
      <h2>About this product</h2>
{body}
      <h2>Typical applications</h2>
      <ul class="apps">
{apps}
      </ul>
    </div>
    <aside class="prod-detail-side">
      <div class="quote-card">
        <h3>Request a price &amp; quote</h3>
        <p>Same-day quotes. Tell us your size, quantity and delivery location.</p>
        <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}WhatsApp quote</a>
        <a class="btn btn-ghost" href="{mailto}">Email this quote</a>
        <a class="btn btn-ghost" href="tel:+254722706416">Call 0722 706 416</a>
        <p class="trust">Direct importer · Deep stock · Spec-matched advice</p>
      </div>
    </aside>
  </section>

  <section class="wrap related">
    <h2>More in {esc(d['name'])}</h2>
    <div class="rel-grid">
{rel_cards}
        <a class="rel-card rel-all" href="{d['slug']}.html"><span>View all {esc(d['name'])} →</span></a>
    </div>
  </section>
</main>

{footer_html("..")}
{fab_mbar_html(f"Hi Kenworks, I would like a quote for: {p['name']}.")}
{COMMON_SCRIPT}
</body>
</html>
'''

# ---------- division page ----------
def render_division(divkey):
    import json
    d = DIVISIONS[divkey]
    canonical = f"{BASE}/products/{d['slug']}.html"
    items = [p for p in PRODUCTS if p["div"] == divkey]
    cards = "\n".join(f'''      <a class="prod-card" href="{p['slug']}.html">
        <div class="prod-card-img"><img src="../images/{p['img']}.jpg" alt="{esc(p['name'])} in Nairobi, Kenya — Kenworks Ventures" loading="lazy" width="640" height="480" /><span class="temp-badge">{esc(p['temp']) if p['temp']!='—' else 'General'}</span></div>
        <div class="prod-card-body"><h3>{esc(p['name'])}</h3><span class="prod-card-cta">View specs &amp; price →</span></div>
      </a>''' for p in items)
    crumb = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
            {"@type": "ListItem", "position": 2, "name": d["name"], "item": canonical},
        ]}
    itemlist = {
        "@context": "https://schema.org", "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": i+1, "name": p["name"], "url": product_url(p)}
            for i, p in enumerate(items)]
    }
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(d["title"])}</title>
<meta name="description" content="{esc(d["meta"])}" />
<meta name="theme-color" content="#0e1a52" />
<link rel="canonical" href="{canonical}" />
<meta property="og:type" content="website" />
<meta property="og:title" content="{esc(d["title"])}" />
<meta property="og:description" content="{esc(d["meta"])}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:site_name" content="Kenworks Ventures" />
<meta name="twitter:card" content="summary_large_image" />
<script type="application/ld+json">{json.dumps(crumb)}</script>
<script type="application/ld+json">{json.dumps(itemlist)}</script>
<script type="application/ld+json">{json.dumps(ORG_JSONLD)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="product.css" />
</head>
<body>
{emblem_defs()}
{header_html("..")}

<main>
  <nav class="breadcrumb wrap" aria-label="Breadcrumb">
    <a href="../index.html">Home</a> <span>›</span>
    <span aria-current="page">{esc(d['name'])}</span>
  </nav>

  <section class="wrap div-head">
    <span class="eyebrow">Division</span>
    <h1>{esc(d['h1'])}</h1>
    <p>{esc(d['intro'])}</p>
    <div class="cta-row">
      <a class="btn btn-wa" href="{wa_link('Hi Kenworks, I would like a quote.')}" target="_blank" rel="noopener">{WA_SVG}Get a quote on WhatsApp</a>
      <a class="btn btn-ghost" href="tel:+254722706416">Call 0722 706 416</a>
    </div>
  </section>

  <section class="wrap div-products">
    <h2>{esc(d['name'])} products</h2>
    <div class="div-grid-cards">
{cards}
    </div>
  </section>
</main>

{footer_html("..")}
{fab_mbar_html("Hi Kenworks, I would like a quote.")}
{COMMON_SCRIPT}
</body>
</html>
'''

ORG_JSONLD = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Kenworks Ventures Company Limited",
    "url": f"{BASE}/",
    "logo": f"{BASE}/images/firebrick-70.jpg",
    "telephone": "+254722706416",
    "email": EMAIL,
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Along Old Enterprise Road, Inside Hema House, Godown No. 8, Industrial Area",
        "postOfficeBoxNumber": "22750-00400",
        "addressLocality": "Nairobi",
        "addressCountry": "KE"
    },
    "areaServed": ["Kenya", "Uganda", "Tanzania", "Rwanda"]
}

# ---------- sitemap + robots ----------
def render_sitemap():
    urls = [f"{BASE}/"]
    for d in DIVISIONS.values():
        urls.append(f"{BASE}/products/{d['slug']}.html")
    for p in PRODUCTS:
        urls.append(product_url(p))
    body = "\n".join(
        f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{'1.0' if u==BASE+'/' else '0.8'}</priority></url>"
        for u in urls)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
'''

def render_robots():
    return f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n"

def main():
    os.makedirs(PRODUCTS_DIR, exist_ok=True)
    written = []
    for p in PRODUCTS:
        path = os.path.join(PRODUCTS_DIR, f"{p['slug']}.html")
        open(path, "w", encoding="utf-8").write(render_product(p))
        written.append(f"products/{p['slug']}.html")
    for k in DIVISIONS:
        path = os.path.join(PRODUCTS_DIR, f"{DIVISIONS[k]['slug']}.html")
        open(path, "w", encoding="utf-8").write(render_division(k))
        written.append(f"products/{DIVISIONS[k]['slug']}.html")
    css_src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "product.css")
    if os.path.exists(css_src):
        import shutil
        shutil.copy(css_src, os.path.join(PRODUCTS_DIR, "product.css"))
        written.append("products/product.css")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(render_sitemap())
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(render_robots())
    written += ["sitemap.xml", "robots.txt"]
    print(f"Generated {len(PRODUCTS)} product pages + {len(DIVISIONS)} division pages.")
    for w in written:
        print("  ", w)

if __name__ == "__main__":
    main()
