/** Dependency-free smoke tests for the FORMA static demo. Run: node tests/smoke.test.js */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const code = fs.readFileSync(path.join(__dirname, '..', 'app.js'), 'utf8');
const html = {innerHTML: '', querySelector:()=>null};
const overlay = {innerHTML: '', querySelector:()=>null};
const toasts={append(){}};
const store = {}, session = {}, handlers = {};
const storage = obj => ({getItem:k=>obj[k]??null,setItem:(k,v)=>{obj[k]=String(v)},removeItem:k=>{delete obj[k]}});
const ctx = {
  console, URLSearchParams, setTimeout, clearTimeout, Date, Math, JSON,
  localStorage:storage(store), sessionStorage:storage(session),
  document:{title:'',body:{classList:{toggle(){}}},querySelector:sel=>sel==='#app'?html:sel==='#ui-layer'?overlay:sel==='#toast-region'?toasts:null,createElement:()=>({classList:{add(){}},remove(){}}),addEventListener:(name,fn)=>{(handlers[name]??=[]).push(fn)}},
  location:{hash:'#/'}, navigator:{},
  window:{addEventListener:(name,fn)=>{(handlers['window:'+name]??=[]).push(fn)},scrollTo(){}},
  confirm:()=>true,
  FormData:class { constructor(form){this.values=form.values||{}} get(key){return this.values[key]??null} }
};
vm.createContext(ctx);vm.runInContext(code,ctx);
const run = expression => vm.runInContext(expression,ctx);
function page(route, text){ctx.location.hash='#'+route;run("if(routePath()==='/shop')parseShopURL();render()");assert.ok(html.innerHTML.includes(text),`Expected ${text} on ${route}`)}
page('/','hero-copy');page('/shop','shop-layout');page('/product/1','detail-layout');page('/collections','collections-page');page('/about','faq-section');page('/wishlist','empty-state');page('/account','empty-state');page('/checkout','empty-state');page('/admin','admin-login');
assert.equal(run('products().length'),20,'seed catalog has 20 products');
run('state.shop.category="Audio"');assert.equal(run('filteredProducts().length'),4,'category filter');
run('state.shop.category="All";state.shop.query="headphones"');assert.equal(run('filteredProducts().length'),2,'keyword filter');
run('state.shop.query="";state.shop.onlySale=true');assert.ok(run('filteredProducts().every(p=>p.compareAt>0)'),'sale-only filter');
run('state.shop.onlySale=false; state.cart=[]; addToCart(1,1,false)');assert.equal(run('cartCount()'),1,'add to cart');
run('state.coupon="FORM10"');assert.equal(run('discount()'),24.9,'coupon discount');
run('toggleWishlist(1)');assert.equal(run('state.wishlist.includes(1)'),true,'wishlist addition');
run('toggleCompare(1)');assert.equal(run('state.compare.includes(1)'),true,'product comparison');
page('/checkout','checkout-form');
const form={id:'checkout-form',values:{email:'example@example.com',firstName:'Alex',lastName:'Tester',address:'123 Sample Lane',city:'Colombo',postal:'10100',country:'Sri Lanka'},reportValidity:()=>true};
handlers.submit[0]({target:form,preventDefault(){}});
assert.equal(run('state.orders.length'),1,'demo checkout saves order');
assert.equal(run('cartCount()'),0,'checkout empties bag');
assert.ok(html.innerHTML.includes('ORDER CONFIRMED'),'checkout success displayed');
const login={id:'admin-login',values:{email:'admin@forma.demo',password:'demo1234'}};
handlers.submit[0]({target:login,preventDefault(){}});
assert.equal(run('state.adminAuthorized'),true,'admin demo login');
page('/admin','admin-metrics');run('state.adminView="products"');page('/admin','inventory-table');run('state.adminView="orders"');page('/admin','admin-orders-table');
assert.equal(run('state.orders.length'),1);
console.log('✓ 9 pages, product filters, cart, coupon, wishlist, comparison, checkout, and admin demo — PASS');
