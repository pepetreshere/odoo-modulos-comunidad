<html>
<head>
  <style type="text/css">
    ${css}
  </style>
</head>
<body>
  <h1>${objects[0]._description or ''|entity}</h1>
  <% setLang(lang) %>
	
  <table class="list_table"  width="100%">
    <thead>
	  <tr>
		<th width="10%">${_("Move")}</th>
		<th width="21%">${_("Name")}</th>
		<th width="6%">${_("Effective Date")}</th>
		<th width="6%">${_("Period")}</th>
		<th width="18%">${_("Partner")}</th>
		<th width="6%">${_("Account")}</th>
		<th width="6%">${_("Mat.Date")}</th>
		<th width="9%" class="amount">${_("Debit")}</th>
		<th width="9%" class="amount">${_("Credit")}</th>
		<th width="9%" class="amount">${_("Amount Curr.")}</th>
	  </tr>
    </thead>
      <tbody>
      %for line in objects:
		<tr>
		  <td>${line.move_id.name or ''|entity}</td>
		  <td>${line.name or ''|entity}</td>
		  <td>${formatLang(line.date, date=True)|entity}</td>
		  <td>${line.period_id.code or ''|entity}</td>
		  <td>${line.partner_id and line.partner_id.name or ''|entity}</td>
		  <td>${line.account_id.code}</td>
		  <td>${formatLang(line.date_maturity, date=True)}</td>
		  <td class="amount">${formatLang(line.debit or 0.0, monetary=True, currency_obj=company.currency_id)}</td>
		  <td class="amount">${formatLang(line.credit or 0.0, monetary=True, currency_obj=company.currency_id)}</td>
		  %if line.currency_id and line.currency_id != company.currency_id:
		    <td class="amount">${line.amount_currency and formatLang(line.amount_currency, monetary=True, currency_obj=line.currency_id) or ''}</td>
		  %endif
		</tr>
      %endfor
        </tbody>
        <tfoot>
		  <tr>
		    <td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td class="amount">${formatLang(sum_debit, monetary=True, currency_obj=company.currency_id)}</td>
			<td class="amount">${formatLang(sum_credit, monetary=True, currency_obj=company.currency_id)}</td>
			<td></td>
		  </tr>
          <tr>
		    <td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td></td>
			<td class="amount">${_("Balance")}</td>
			<td class="amount">${formatLang(sum_debit - sum_credit, monetary=True, currency_obj=company.currency_id)}</td>
			<td></td>
          </tr>
		</tfoot>
  </table>
  %if sum_amount_currency:
    <br>
    <p style="font-weight:bold;font-size:11;">${_("Totals in Foreign Currencies") + ':'}</p>
    <table class="list_table" width="20%" empty-cells="show">
      <thead>
	  <tr>
		<th>${_("Foreign Currency")}</th>
		<th>${_("Company Currency")}</th>
		<th></th>
	  </tr>
      </thead>
      <tbody>
	    %for entry in sum_amount_currency:
	      <tr>
    		<td>${formatLang(entry['sum_foreign'], monetary=True, currency_obj=entry['currency'])}</td>
    		<td>${formatLang(entry['sum'], monetary=True, currency_obj=company.currency_id)}</td>
    		<td></td>
	      </tr>
        %endfor
      <tbody>

    </table>
  %endif	
	
</body>
</html>
